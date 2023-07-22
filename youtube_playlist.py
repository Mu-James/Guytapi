import personal
from build import build_youtube

def get_all_channel_public_playlists(yt_channel_id, yt_api_key=personal.yt_api_key):
    youtube = build_youtube(yt_api_key)

    request = youtube.playlists().list(
        part="contentDetails",
        channelId=yt_channel_id,
        maxResults=25
    )

    response = request.execute()

    return response

def get_playlist_data(playlist_id, yt_api_key=personal.yt_api_key):
    youtube = build_youtube(yt_api_key)

    request = youtube.playlists().list(
        part="contentDetails",
        id=playlist_id
    )

    response = request.execute()

    return response

def print_playlist_video_titles(playlist_id, yt_api_key=personal.yt_api_key):
    youtube = build_youtube(yt_api_key)

    request = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlist_id,
        maxResults=5
    )

    response = request.execute()

    playlistItems = response['items']
    nextPageToken = response.get('nextPageToken')

    while nextPageToken:
        request = youtube.playlistItems().list(
            part="snippet",
            playlistId=playlist_id,
            maxResults=5,
            pageToken=nextPageToken
        )

        response = request.execute()

        playlistItems.extend(response['items'])
        nextPageToken = response.get('nextPageToken')

    for video in playlistItems:
        print(video['snippet']['title'])

