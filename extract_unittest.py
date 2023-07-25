import unittest as ut
import extract as e


class TestExtractMethods(ut.TestCase):

    def test_generate_url_general(self):
        e._generate_request("https://www.google.com/")
        self.assertEqual(True, True)

    def test_generate_url_yt(self):
        e._generate_request("https://www.youtube.com/")
        self.assertEqual(True, True)

    def test_generate_url_yt_video(self):
        e._generate_request("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        self.assertEqual(True, True)

    def test_generate_url_yt_channel(self):
        e._generate_request("https://www.youtube.com/@YouTube")
        self.assertEqual(True, True)

    def test_generate_url_invalid_general(self):
        with self.assertRaises(Exception):
            e._generate_request("google")
        
        
if __name__ == "__main__":
    ut.main()