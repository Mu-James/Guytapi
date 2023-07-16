import personal

from googleapiclient.discovery import build

api_service_name = 'youtube'
api_version = 'v3'

def get_all_channel_public_playlists(yt_api_key, yt_channel_id):

    youtube = build(api_service_name, api_version, developerKey=yt_api_key)

    request = youtube.playlists().list(
        part="contentDetails",
        channelId=yt_channel_id,
        maxResults=25
    )

    response = request.execute()

    return response