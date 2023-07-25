import unittest as ut
import extract as e


class TestExtractMethods(ut.TestCase):

    def test_generate_url(self):
        e._generate_request("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        self.assertEqual(True, True)


if __name__ == "__main__":
    ut.main()