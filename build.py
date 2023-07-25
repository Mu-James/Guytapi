from googleapiclient.discovery import build

YT_SERVICE = "youtube"
YT_VERSION = 'v3'


def build_youtube(yt_api_key):
    api_service_name = YT_SERVICE
    api_version = YT_VERSION

    return build(api_service_name, api_version, developerKey=yt_api_key)