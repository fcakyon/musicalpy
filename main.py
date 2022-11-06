from pytube import YouTube
from moviepy.editor import *

music_url_or_path = "https://www.youtube.com/watch?v=_CL6n0FJZpk"
video_url_or_path = "WhatsApp Video 2022-11-06 at 12.51.03.mp4"

music_delay = 7.5
music_offset = 31
video_offset = 0
end_seconds = 10

if 'youtube' in music_url_or_path:
    music_filepath = YouTube(music_url_or_path).streams.filter(only_audio=True).order_by('abr').desc().first().download()
else:
    music_filepath = music_url_or_path

if 'youtube' in video_url_or_path:
    video_filepath = YouTube(video_url_or_path).streams.filter(progressive=True).order_by('resolution').desc().first().download()
else:
    video_filepath = video_url_or_path

video_videoclip = VideoFileClip(video_filepath)
music_audioclip = AudioFileClip(music_filepath)
video_audioclip = AudioFileClip(video_filepath)

audio_end_time = video_videoclip.duration - music_delay

mixed_audioclip = CompositeAudioClip(
    [
        video_audioclip.subclip(start_time=video_offset).multiply_volume(1),
        music_audioclip.subclip(start_time=music_offset, end_time=music_offset+end_seconds-music_delay).with_start(music_delay),
    ]
)

final_videoclip = video_videoclip.subclip(start_time=video_offset).with_audio(mixed_audioclip)

final_videoclip.write_videofile("final.mp4", audio_codec="aac")