import urllib.request
from urllib.parse import urlparse

YT_URL = "www.youtube.com"
YT_URL_SHORT = "youtu.be"

def _generate_request(url):
    try:
        return urllib.request.Request(url)
    except Exception as e:
        raise e
    
def _get_host(url):
    return urlparse(url).hostname

def _get_video_id(query):
    return query[2:]

def _get_url_query(url):
    return urlparse(url).query

def extract_youtube_video_id_from_url(url):
    try:
        host = _get_host(url)

        if host == YT_URL or host == YT_URL_SHORT:
            return _get_video_id(_get_url_query(url))

    except Exception as e:
        raise e
