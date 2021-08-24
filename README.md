### install dependencies

`pip install -r requirements.txt`

### anonymize video with gluoncv models

`python anonymize_with_gluoncv.py  {input_path} -m {model_name}`

example: `python anonymize.py examples/Ch2_001_CH013_V_cut_frames.MP4 -m deeplab_resnet101_voc`

### anonymize video with Unet model

`python anonymize_with_Unet.py`

### Output directory

anonymized videos are stored in anonymized_video folder

