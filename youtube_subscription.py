import personal
from build import build_youtube

#Subscriptions must not be set to private to work
def get_subscriptions_with_datetime(yt_channel_id, yt_api_key=personal.yt_api_key):
    youtube = build_youtube(yt_api_key)

    request = youtube.subscriptions().list(
        part="snippet",
        channelId=yt_channel_id
    )

    response = request.execute()

    return response