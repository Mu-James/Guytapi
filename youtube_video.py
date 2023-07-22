import personal
from build import build_youtube

def get_video_thumbnail_url(video_id, size, yt_api_key=personal.yt_api_key):
    youtube = build_youtube(yt_api_key)

    request = youtube.videos().list(
        part="snippet",
        id=video_id
    )

    response = request.execute()
    video = response['items']
    return video[0]['snippet']['thumbnails'][size]['url']

def get_video_view_count(video_id, yt_api_key=personal.yt_api_key):
    youtube = build_youtube(yt_api_key)
    
    request = youtube.videos().list(
        part="statistics",
        id=video_id
    )

    response = request.execute()
    video = response['items']
    return video[0]['statistics']['viewCount']
