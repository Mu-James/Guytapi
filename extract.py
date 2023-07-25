import urllib.request

def _generate_request(url):
    try:
        return urllib.request.Request(url)
    except Exception as e:
        raise e
    
def _get_host(url):
    return _generate_request(url).origin_req_host

def extract_youtube_video_id_from_url(url):
    host = _get_host(url)

