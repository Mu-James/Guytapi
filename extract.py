import urllib.request
from urllib.parse import urlparse
import requests as r

YT_URL = "www.youtube.com"
YT_URL_SHORT = "youtu.be"
_LEN_CHANNEL_ID_STRING = 12

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

def _get_http_response_text(url):
    return r.get(url).text

def _find_index_channel_id(response_text):
    index = response_text.find("?channel_id=")
    index += _LEN_CHANNEL_ID_STRING
    return index

def extract_youtube_channel_id_from_url(url):
    id = ""

    response = _get_http_response_text(url)
    index = _find_index_channel_id(response)

    while response[index] != '"':
        id += response.text[index]
        index += 1

    return id

