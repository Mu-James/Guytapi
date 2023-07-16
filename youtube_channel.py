import personal

from googleapiclient.discovery import build

"""
api_service_name = 'youtube'
api_version = 'v3'

youtube = build(api_service_name, api_version, developerKey=personal.yt_api_key)

request = youtube.channels().list(
        part='statistics',
        id=personal.yt_id
    )

response = request.execute()

print(response)
"""