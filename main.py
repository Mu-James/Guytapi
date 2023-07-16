import youtube_channel as yc
import youtube_playlist as yp
import personal

if __name__ == "__main__":
    print(yp.get_all_channel_public_playlists(personal.yt_channel_id, personal.yt_api_key))
    print(yp.get_playlist_data(personal.yt_playlist_id, personal.yt_api_key))
    yp.print_playlist_video_titles(personal.yt_playlist_id, personal.yt_api_key)