import unittest as ut
import extract as e

class TestGeneratetUrl(ut.TestCase):
    def test_generate_url_general(self):
        e._generate_request("https://www.google.com/")
        self.assertEqual(True, True)

    def test_generate_url_yt(self):
        e._generate_request("https://www.youtube.com/")
        self.assertEqual(True, True)

    def test_generate_url_yt_shortened(self):
        e._generate_request("http://youtu.be/")
        self.assertEqual(True, True)

    def test_generate_url_yt_video(self):
        e._generate_request("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        self.assertEqual(True, True)

    def test_generate_url_yt_video_shortened(self):
        e._generate_request("https://youtu.be/bKjAj9Lc674")
        self.assertEqual(True, True)

    def test_generate_url_yt_channel(self):
        e._generate_request("https://www.youtube.com/@YouTube")
        self.assertEqual(True, True)

    def test_generate_url_general_invalid(self):
        with self.assertRaises(Exception):
            e._generate_request("google")
        
class TestGetHost(ut.TestCase):
    def test_get_host_general(self):
        self.assertEqual(e._get_host("https://github.com"), "github.com")

    def test_get_host_general_subdirectory(self):
        self.assertEqual(e._get_host("https://github.com/login"), "github.com")

    def test_get_host_yt(self):
        self.assertEqual(e._get_host("https://www.youtube.com/"), "www.youtube.com")

    def test_get_host_yt_video(self):
        self.assertEqual(e._get_host("https://www.youtube.com/watch?v=Iz3K7wkJx4E"), "www.youtube.com")

    def test_get_host_yt_video_shortened(self):
        self.assertEqual(e._get_host("https://youtu.be/Iz3K7wkJx4E"), "youtu.be") 

class TestGetYTVideoID(ut.TestCase):
    def test_extract_yt_video_id_from_url(self):
        self.assertEqual(e.extract_youtube_video_id_from_url("https://www.youtube.com/watch?v=XxbJw8PrIkc"), "XxbJw8PrIkc")

    def test_extract_yt_video_id_from_url_wrong_host(self):
        with self.assertRaises(e.NotYoutubeHostException):
            e.extract_youtube_video_id_from_url("www.google.com")

class TestGetYTPlaylistID(ut.TestCase):
    def test_extract_yt_video_id_from_url(self):
        self.assertEqual(e.extract_youtube_playlist_id_from_url("https://www.youtube.com/playlist?list=PL1qnH1TrDn6vdogf2DKrQy2lnyo_HvTdj"), "PL1qnH1TrDn6vdogf2DKrQy2lnyo_HvTdj")

    def test_extract_yt_video_id_from_url_wrong_host(self):
        with self.assertRaises(e.NotYoutubeHostException):
            e.extract_youtube_playlist_id_from_url("www.google.com")
            
if __name__ == "__main__":
    ut.main()
    