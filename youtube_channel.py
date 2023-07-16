import personal
from googleapiclient.discovery import build

def get_channel_statisitcs(yt_channel_id, yt_api_key=personal.yt_api_key):
    api_service_name = 'youtube'
    api_version = 'v3'

    youtube = build(api_service_name, api_version, developerKey=yt_api_key)

    request = youtube.channels().list(
            part='statistics',
            id=yt_channel_id
        )

    response = request.execute()

    return response
