import personal
from build import build_youtube

def get_channel_statisitcs(yt_channel_id, yt_api_key=personal.yt_api_key):
    youtube = build_youtube(yt_api_key)

    request = youtube.channels().list(
            part='statistics',
            id=yt_channel_id
        )

    response = request.execute()

    return response
