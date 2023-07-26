import urllib.request
from urllib.parse import urlparse

YT_URL = "www.youtube.com"
YT_URL_SHORT = "youtu.be"

class NotYoutubeHostException(Exception):
    def __init__(self, *args, **kwargs):
        message = "Exception occurred: Non-Youtube host detected"
        super().__init__(message)

def _generate_request(url):
    try:
        return urllib.request.Request(url)
    except Exception as e:
        raise e
    
def _get_host(url):
    return urlparse(url).hostname

def _get_video_id(query):
    return query[2:]

def _get_playlist_id(query):
    return query[5:]

def _get_url_query(url):
    return urlparse(url).query

def _is_yt_host(host):
    return host == YT_URL or host == YT_URL_SHORT

def extract_youtube_video_id_from_url(url):
    try:
        host = _get_host(url)

        if _is_yt_host(host):
            return _get_video_id(_get_url_query(url))
        else:
            raise NotYoutubeHostException

    except Exception as e:
        raise e
    
def extract_youtube_playlist_id_from_url(url):
    try:
        host = _get_host(url)

        if _is_yt_host(host):
            return _get_playlist_id(_get_url_query(url))
        else:
            raise NotYoutubeHostException
        
    except Exception as e:
        raise e
