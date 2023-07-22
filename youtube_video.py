import personal
from build import build_youtube

def get_video_thumbnail(video_id, yt_api_key=personal.yt_api_key):
    youtube = build_youtube(yt_api_key)