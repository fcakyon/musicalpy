<p align="center">
  <img src="https://user-images.githubusercontent.com/34196005/200189651-dbe16be4-0dc5-47a0-b0ff-730a2b162c85.jpg" width="150" height="150" />
</p>

<h1 align="center">musicalpy</h1>

A simple way of combining a music and a video (logo is a random [stable diffusion](https://huggingface.co/spaces/stabilityai/stable-diffusion) generation)

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