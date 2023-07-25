import urllib.request

def _generate_request(url):
    return urllib.request.Request(url)

def extract_youtube_video_id_from_url(url):
    try:
        yt_url = _generate_request(url)
    except Exception as error:
        print(error)
