import build as b

def verify_api_key(yt_api_key):
    try:
        verify = b.build_youtube(yt_api_key)
        request = verify.i18nRegions().list(
            part="snippet"
        )
        response = request.execute()
        return True
    except Exception as e:
        return e._get_reason()