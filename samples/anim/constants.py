SMPL_BODY_BONES = [
    'pelvis',
    'left_hip',
    'right_hip',
    'spine1',
    'left_knee',
    'right_knee',
    'spine2',
    'left_ankle',
    'right_ankle',
    'spine3',
    'left_foot',
    'right_foot',
    'neck',
    'left_collar',
    'right_collar',
    'head',
    'left_shoulder',
    'right_shoulder',
    'left_elbow',
    'right_elbow',
    'left_wrist',
    'right_wrist',
    # smpl only. But without corresponding bone.
    # 'left_hand',
    # 'right_hand',
    # head
    'jaw',
    # 'left_eyeball',
    # 'right_eyeball',
    'left_eye_smplhf',
    'right_eye_smplhf',
]
SMPL_FINGER_BONES = [
    # left hand
    'left_index1',
    'left_index2',
    'left_index3',
    'left_middle1',
    'left_middle2',
    'left_middle3',
    'left_pinky1',
    'left_pinky2',
    'left_pinky3',
    'left_ring1',
    'left_ring2',
    'left_ring3',
    'left_thumb1',
    'left_thumb2',
    'left_thumb3',
    # right hand
    'right_index1',
    'right_index2',
    'right_index3',
    'right_middle1',
    'right_middle2',
    'right_middle3',
    'right_pinky1',
    'right_pinky2',
    'right_pinky3',
    'right_ring1',
    'right_ring2',
    'right_ring3',
    'right_thumb1',
    'right_thumb2',
    'right_thumb3',
]

SMPLX_JOINT_NAMES = [
    'pelvis',
    'left_hip',
    'right_hip',
    'spine1',
    'left_knee',
    'right_knee',
    'spine2',
    'left_ankle',
    'right_ankle',
    'spine3',
    'left_foot',
    'right_foot',
    'neck',
    'left_collar',
    'right_collar',
    'head',
    'left_shoulder',
    'right_shoulder',
    'left_elbow',
    'right_elbow',
    'left_wrist',
    'right_wrist',
    'jaw',
    'left_eye_smplhf',
    'right_eye_smplhf',
    'left_index1',
    'left_index2',
    'left_index3',
    'left_middle1',
    'left_middle2',
    'left_middle3',
    'left_pinky1',
    'left_pinky2',
    'left_pinky3',
    'left_ring1',
    'left_ring2',
    'left_ring3',
    'left_thumb1',
    'left_thumb2',
    'left_thumb3',
    'right_index1',
    'right_index2',
    'right_index3',
    'right_middle1',
    'right_middle2',
    'right_middle3',
    'right_pinky1',
    'right_pinky2',
    'right_pinky3',
    'right_ring1',
    'right_ring2',
    'right_ring3',
    'right_thumb1',
    'right_thumb2',
    'right_thumb3',
]
NUM_SMPLX_JOINTS = len(SMPLX_JOINT_NAMES)
NUM_SMPLX_BODYJOINTS = 21
NUM_SMPLX_HANDJOINTS = 15

SMPLX_HAND_POSES = {
    'flat': [
        [
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
        ],
        [
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
        ],
    ],
    'relaxed': [
        [
            0.11167871206998825,
            0.042892176657915115,
            -0.41644182801246643,
            0.10881132632493973,
            -0.06598567962646484,
            -0.7562199831008911,
            -0.09639296680688858,
            -0.09091565757989883,
            -0.18845929205417633,
            -0.1180950403213501,
            0.050943851470947266,
            -0.529584527015686,
            -0.14369840919971466,
            0.055241700261831284,
            -0.7048571109771729,
            -0.01918291673064232,
            -0.09233684837818146,
            -0.33791351318359375,
            -0.4570329785346985,
            -0.1962839514017105,
            -0.6254575252532959,
            -0.21465237438678741,
            -0.06599828600883484,
            -0.5068942308425903,
            -0.3697243630886078,
            -0.060344625264406204,
            -0.07949022948741913,
            -0.1418696939945221,
            -0.08585263043642044,
            -0.6355282664299011,
            -0.3033415973186493,
            -0.05788097530603409,
            -0.6313892006874084,
            -0.17612089216709137,
            -0.13209307193756104,
            -0.37335458397865295,
            0.8509643077850342,
            0.27692273259162903,
            -0.09154807031154633,
            -0.4998394250869751,
            0.02655647136271,
            0.05288087576627731,
            0.5355591773986816,
            0.04596104100346565,
            -0.2773580253124237,
        ],
        [
            0.11167871206998825,
            -0.042892176657915115,
            0.41644182801246643,
            0.10881132632493973,
            0.06598567962646484,
            0.7562199831008911,
            -0.09639296680688858,
            0.09091565757989883,
            0.18845929205417633,
            -0.1180950403213501,
            -0.050943851470947266,
            0.529584527015686,
            -0.14369840919971466,
            -0.055241700261831284,
            0.7048571109771729,
            -0.01918291673064232,
            0.09233684837818146,
            0.33791351318359375,
            -0.4570329785346985,
            0.1962839514017105,
            0.6254575252532959,
            -0.21465237438678741,
            0.06599828600883484,
            0.5068942308425903,
            -0.3697243630886078,
            0.060344625264406204,
            0.07949022948741913,
            -0.1418696939945221,
            0.08585263043642044,
            0.6355282664299011,
            -0.3033415973186493,
            0.05788097530603409,
            0.6313892006874084,
            -0.17612089216709137,
            0.13209307193756104,
            0.37335458397865295,
            0.8509643077850342,
            -0.27692273259162903,
            0.09154807031154633,
            -0.4998394250869751,
            -0.02655647136271,
            -0.05288087576627731,
            0.5355591773986816,
            -0.04596104100346565,
            0.2773580253124237,
        ],
    ],
}

SMPL_IDX_TO_JOINTS = (
    (0, 'Pelvis'),
    (1, 'Hip_L'),
    (2, 'Hip_R'),
    (3, 'Spine1'),
    (4, 'Knee_L'),
    (5, 'Knee_R'),
    (6, 'Spine2'),
    (7, 'Ankle_L'),
    (8, 'Ankle_R'),
    (9, 'Chest'),
    (10, 'Toes_L'),
    (11, 'Toes_R'),
    (12, 'Neck'),
    (13, 'Scapula_L'),
    (14, 'Scapula_R'),
    (15, 'Head'),
    (16, 'Shoulder_L'),
    (17, 'Shoulder_R'),
    (18, 'Elbow_L'),
    (19, 'Elbow_R'),
    (20, 'Wrist_L'),
    (21, 'Wrist_R'),
    (22, ''),
    (23, ''),
)
SMPL_PARENT_IDX = (
    -1,
    0,
    0,
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    12,
    12,
    12,
    13,
    14,
    16,
    17,
    18,
    19,
    20,
    21,
)

SMPLX_IDX_TO_JOINTS = (
    (0, 'Pelvis'),
    (1, 'Hip_L'),
    (2, 'Hip_R'),
    (3, 'Spine1'),
    (4, 'Knee_L'),
    (5, 'Knee_R'),
    (6, 'Spine2'),
    (7, 'Ankle_L'),
    (8, 'Ankle_R'),
    (9, 'Chest'),
    (10, 'Toes_L'),
    (11, 'Toes_R'),
    (12, 'Neck'),
    (13, 'Scapula_L'),
    (14, 'Scapula_R'),
    (15, 'Head'),
    (16, 'Shoulder_L'),
    (17, 'Shoulder_R'),
    (18, 'Elbow_L'),
    (19, 'Elbow_R'),
    (20, 'Wrist_L'),
    (21, 'Wrist_R'),
    (22, 'index_A_L'),
    (23, 'index_B_L'),
    (24, 'index_C_L'),
    (25, 'middle_A_L'),
    (26, 'middle_B_L'),
    (27, 'middle_C_L'),
    (28, 'pinky_A_L'),
    (29, 'pinky_B_L'),
    (30, 'pinky_C_L'),
    (31, 'ring_A_L'),
    (32, 'ring_B_L'),
    (33, 'ring_C_L'),
    (34, 'thumb_A_L'),
    (35, 'thumb_B_L'),
    (36, 'thumb_C_L'),
    (37, 'index_A_R'),
    (38, 'index_B_R'),
    (39, 'index_C_R'),
    (40, 'middle_A_R'),
    (41, 'middle_B_R'),
    (42, 'middle_C_R'),
    (43, 'pinky_A_R'),
    (44, 'pinky_B_R'),
    (45, 'pinky_C_R'),
    (46, 'ring_A_R'),
    (47, 'ring_B_R'),
    (48, 'ring_C_R'),
    (49, 'thumb_A_R'),
    (50, 'thumb_B_R'),
    (51, 'thumb_C_R'),
)
SMPLX_PARENT_IDX = (
    -1,
    0,
    0,
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    12,
    12,
    12,
    13,
    14,
    16,
    17,
    18,
    19,
    20,
    21,
    # left hand
    20,
    22,
    23,
    20,
    25,
    26,
    20,
    28,
    29,
    20,
    31,
    32,
    20,
    34,
    35,
    # right hand
    21,
    37,
    38,
    21,
    40,
    41,
    21,
    43,
    44,
    21,
    46,
    47,
    21,
    49,
    50,
)
