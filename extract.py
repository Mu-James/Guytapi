import urllib

def extract_youtube_video_id_from_url(url):
    try:
        url_request = urllib.request.Request(url)
    except:
        print("Error: Invalid URL")
        