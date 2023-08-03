import googleapiclient as gac
import google as g
import build as b

def verify_api_key(yt_api_key):
    try:
        if yt_api_key == "":
            return "Invalid key: Key cannot be empty"
        verify = b.build_youtube(yt_api_key)
        request = verify.i18nRegions().list(
            part="snippet"
        )
        response = request.execute()
        return True
    except gac.errors.HttpError as e:
        return e._get_reason()
    except g.auth.exceptions.DefaultCredentialsError as e:
        return e