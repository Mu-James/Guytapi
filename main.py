import youtube_channel as yc
import youtube_playlist as yp
import personal

if __name__ == "__main__":
    print(yp.get_all_channel_public_playlists(personal.yt_api_key, personal.yt_channel_id))
