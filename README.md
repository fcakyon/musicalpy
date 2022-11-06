# musicalpy
Easiest way of combining a music and a video

## installation

```bash
git clone https://github.com/fcakyon/musicalpy.git
pip install -r requirements.txt
```

## usage

set params in `main.py` and run it with python

```bash
python main.py
```

## params

`video_url_or_path`: youtube url or local path for base video
`music_url_or_path`: youtube url or local path for music to be mixed

`video_offset`: set to clip the starting seconds of video
`music_delay`: at which second should music start to play
`music_offset`: set to clip the starting seconds of music
`end_seconds`: max length of output video