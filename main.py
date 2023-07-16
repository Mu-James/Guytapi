import youtube_channel as yc
import youtube_playlist as yp
import youtube_subscription as ys
import personal

if __name__ == "__main__":
    print(yc.get_channel_statisitcs(personal.yt_channel_id, personal.yt_api_key))
    print(yp.get_all_channel_public_playlists(personal.yt_channel_id, personal.yt_api_key))
    print(yp.get_playlist_data(personal.yt_playlist_id, personal.yt_api_key))
    yp.print_playlist_video_titles(personal.yt_playlist_id, personal.yt_api_key)
    print(ys.get_subscriptions_at_datetime(personal.yt_channel_id, personal.yt_api_key))