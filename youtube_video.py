import personal
import extract as e
from build import build_youtube

def get_video_thumbnail_url_id(video_id, size, yt_api_key=personal.yt_api_key):
    youtube = build_youtube(yt_api_key)

    request = youtube.videos().list(
        part="snippet",
        id=video_id
    )

    response = request.execute()
    video = response['items']
    return video[0]['snippet']['thumbnails'][size]['url']

def get_video_view_count_id(video_id, yt_api_key=personal.yt_api_key):
    youtube = build_youtube(yt_api_key)
    
    request = youtube.videos().list(
        part="statistics",
        id=video_id
    )

    response = request.execute()
    video = response['items']
    return video[0]['statistics']['viewCount']

def get_video_view_count_url(url, yt_api_key, size):
    video_id = e.extract_youtube_video_id_from_url(url)
    return get_video_view_count_id(video_id, size, yt_api_key)

def get_video_thumbnail_url_url(url, yt_api_key):
    video_id = e.extract_youtube_video_id_from_url(url)
    return get_video_thumbnail_url_id(video_id, yt_api_key)