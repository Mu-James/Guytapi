import personal
from build import build_youtube
import extract as e

def get_channel_statisitcs_id(yt_channel_id, yt_api_key=personal.yt_api_key):
    youtube = build_youtube(yt_api_key)

    request = youtube.channels().list(
            part='statistics',
            id=yt_channel_id
        )

    response = request.execute()

    return response

def get_channel_statistics_url(url, yt_api_key):
    channel_id = e.extract_youtube_channel_id_from_url(url)
    return get_channel_statisitcs_id(channel_id, yt_api_key)

def get_parsed_channel_statistics_response(channel_statistics_response):
    stats = channel_statistics_response['items'][0]['statistics']

    parsed = f"View Count: {stats['viewCount']}\n"

    if stats['hiddenSubscriberCount'] != True:
        parsed += f"Subscriber Count: {stats['subscriberCount']}\n"

    parsed += f"Video Count: {stats['videoCount']}"

    return parsed