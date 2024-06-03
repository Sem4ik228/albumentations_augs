# Copyright (c) OpenMMLab. All rights reserved.
_base_ = ['../../configs/_base_/models/tsn_r50.py']

# dataset settings
dataset_type = 'VideoDataset'
test_pipeline = [
    dict(type='DecordInit'),
    dict(
        type='SampleFrames',
        clip_len=1,
        frame_interval=1,
        num_clips=8,
        test_mode=True),
    dict(type='DecordDecode'),
    dict(type='Resize', scale=(-1, 256)),
    dict(type='CenterCrop', crop_size=224),
    dict(type='RandomSunFlare', src_radius=100, src_colors=[(0, 0, 0), (255, 255, 255)], p=1.0),
    dict(type='RandomSnow', snow_point_lower=0.1, snow_point_upper=0.3, brightness_coeff=(0.5, 2.5), p=1.0),
    dict(type='PitchAndTwirl', severity=(5.5, 10.0), p=1.0),
    dict(type='Sparkles', severity=(1.0, 6.0), p=1.0),
    dict(type='RandomGrayWithCompression', quality_lower=30, quality_upper=95, p=1.0),
    dict(type='InverseSparkles', severity=(1.0, 10.0), color=[[255, 255, 255], [0, 0, 0]], p=1.0),
    dict(type='FormatShape', input_format='NCHW'),
    dict(type='PackActionInputs')
]

test_dataloader = dict(
    batch_size=1,
    num_workers=2,
    dataset=dict(
        type=dataset_type,
        ann_file=None,
        data_prefix=None,
        pipeline=test_pipeline))
