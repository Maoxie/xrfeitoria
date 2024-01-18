import argparse
import json
import shutil
from pathlib import Path
from textwrap import dedent
from typing import Literal, Optional

from loguru import logger
from rich.prompt import Prompt

from xrfeitoria.data_structure.constants import tmp_dir
from xrfeitoria.utils.downloader import download
from xrfeitoria.utils.setup import Config, get_exec_path, guess_exec_path
from xrfeitoria.utils.tools import Logger

# XXX: Hard-coded assets url
ASSETS_URL = dict(
    bunny='https://openxrlab-share.oss-cn-hongkong.aliyuncs.com/xrfeitoria/assets/stanford-bunny.obj',
    koupen_chan='https://openxrlab-share.oss-cn-hongkong.aliyuncs.com/xrfeitoria/assets/koupen_chan.fbx',
    SMPL_XL='https://openxrlab-share.oss-cn-hongkong.aliyuncs.com/xrfeitoria/assets/SMPL-XL-001.fbx',
    motion_1='https://openxrlab-share.oss-cn-hongkong.aliyuncs.com/xrfeitoria/assets/motion-greeting.fbx',
    motion_2='https://openxrlab-share.oss-cn-hongkong.aliyuncs.com/xrfeitoria/assets/motion-stand_to_walk_back.fbx',
    blend_sample='https://openxrlab-share.oss-cn-hongkong.aliyuncs.com/xrfeitoria/assets/Tree1.blend',
    hdr_sample='https://openxrlab-share.oss-cn-hongkong.aliyuncs.com/xrfeitoria/assets/hdr-sample.hdr',
)
# XXX: hard-coded unreal project url
UNREAL_SAMPLE_URL = (
    'https://openxrlab-share.oss-cn-hongkong.aliyuncs.com/xrfeitoria/unreal_project/XRFeitoriaUnreal_Sample.zip'
)
asset_dir = tmp_dir / 'assets'


ENGINE_CHOICES = ['blender', 'unreal']


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Setup the environment for the samples.')
    parser.add_argument('--engine', type=str, default=None, choices=ENGINE_CHOICES)
    parser.add_argument('--exec', type=str, default="")
    parser.add_argument('--unreal_project', type=str, default="")
    parser.add_argument('--unattended', action='store_true', default=False)
    return parser.parse_args()


def get_engine() -> str:
    default = ENGINE_CHOICES[0]
    args = parse_arguments()
    if args.engine:
        engine = args.engine
    elif args.unattended:
        engine = default
    else:
        engine = Prompt.ask('Which engine do you want to use?', choices=ENGINE_CHOICES, default=default)
    return engine


def get_exec(engine: Literal['blender', 'unreal'], exec_from_config: Optional[Path] = None) -> str:
    """Ask for blender executable path.

    Args:
        engine (Literal['blender', 'unreal']): Engine name.
        engine_path_from_config (Optional[Path], optional): path of engine executable read from config. Defaults to None.
    """
    txt = f'Please input the path to the {engine} executable'

    # priority: CLI arguments > exec_from_config > system_config (with guess) > ask > install
    args = parse_arguments()
    args_exec = args.exec.strip('"').strip("'")
    if args_exec:
        path = Path(args_exec).resolve()
    else:
        if exec_from_config is not None:
            engine_path = Path(exec_from_config).resolve().as_posix()
        else:
            try:
                # system_config, if empty, guess
                engine_path = get_exec_path(engine=engine, to_ask=False, to_install=False).as_posix()
            except FileNotFoundError:
                engine_path = None
                txt += f' (e.g. {guess_exec_path(engine)})'
                if engine == 'blender':
                    txt += ', or press [bold]enter[/bold] to install it'

        # ask or use default
        if args.unattended:
            path = engine_path
        else:
            path = Prompt.ask(txt, default=engine_path)

        if path is not None:
            path = Path(path.strip('"').strip("'")).resolve()
        else:
            if engine == 'unreal':
                raise FileNotFoundError('Please specify the path to the unreal executable.')
            # auto install for blender
            path = get_exec_path(engine=engine, to_ask=False, to_install=True)

    assert path.exists(), f'{engine} path {path.as_posix()} does not exist!'
    return path.as_posix()


def get_unreal_project(unreal_project: str) -> str:
    """Ask for unreal project path."""
    
    args = parse_arguments()
    args_unreal_project = args.unreal_project.strip('"').strip("'")
    if args_unreal_project:
        unreal_project = Path(args_unreal_project).resolve().as_posix()
    else:
        # ask or use default
        if args.unattended:
            unreal_project = unreal_project
        else:
            txt = 'Please input the path to the unreal project'
            if unreal_project is None:
                txt += ', or press [bold]enter[/bold] to download a sample project\n' '\[Enter]'
            unreal_project = Prompt.ask(txt, default=unreal_project)

        if unreal_project is None:
            unreal_project_zip = download(url=UNREAL_SAMPLE_URL, dst_dir=tmp_dir / 'unreal_project')
            shutil.unpack_archive(filename=unreal_project_zip, extract_dir=tmp_dir / 'unreal_project')
            unreal_project_dir = unreal_project_zip.parent / unreal_project_zip.stem
            unreal_project = next(unreal_project_dir.glob('*.uproject')).as_posix()
        unreal_project = unreal_project.strip('"').strip("'")

    if not Path(unreal_project).exists():
        config_file = Path(__file__).parent / 'config.py'
        logger.error(
            '[red]Error:[/red]\n'
            f'Unreal project "{unreal_project}" does not exist! \n'
            f'Config not set correctly, please [red]delete "{config_file.as_posix()}"[/red], and setup again.'
        )
        exit(1)
    return unreal_project


def main():
    try:
        from .config import blender_exec, unreal_exec, unreal_project
    except ImportError:
        blender_exec = unreal_exec = unreal_project = None

    Logger.setup_logging()
    engine = get_engine()
    if engine == 'blender':
        blender_exec = get_exec('blender', exec_from_config=blender_exec)
        Config.update(engine=engine, exec_path=blender_exec)
    elif engine == 'unreal':
        unreal_exec = get_exec('unreal', exec_from_config=unreal_exec)
        unreal_project = get_unreal_project(unreal_project=unreal_project)
        Config.update(engine=engine, exec_path=unreal_exec)

    assets_path = {}
    for idx, (name, url) in enumerate(ASSETS_URL.items()):
        logger.info(f'Downloading {idx+1}/{len(ASSETS_URL)}: {name}')
        save_path = download(url, dst_dir=asset_dir / name)
        # save the path
        assets_path[name] = save_path.as_posix()

    # write the config file
    config_path = Path(__file__).parent / 'config.py'
    with open(config_path, 'w') as f:
        _keys = {key: 'str' for key in assets_path.keys()}
        _config = dedent(
            f"""\
            from typing import TypedDict

            blender_exec = {repr(blender_exec)}
            unreal_exec = {repr(unreal_exec)}
            unreal_project = {repr(unreal_project)}

            assets_path_type = TypedDict('assets_path', {json.dumps(_keys)})
            assets_path: assets_path_type = {json.dumps(assets_path)}"""
        )
        f.write(_config)
    logger.info(f'Saved config to "{config_path}"')


if __name__ == '__main__':
    main()
