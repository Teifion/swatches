import swatcher
import unittest

class SwatcherMethods(unittest.TestCase):
  def test_known_urls(self):
      urls = [
        ('https://pwintyimages.blob.core.windows.net/samples/stars/test-sample-black.png', 'black'),
        ('https://pwintyimages.blob.core.windows.net/samples/stars/test-sample-grey.png', 'grey'),
        ('https://pwintyimages.blob.core.windows.net/samples/stars/test-sample-teal.png', 'teal'),
        ('https://pwintyimages.blob.core.windows.net/samples/stars/test-sample-navy.png', 'navy')
      ]

      for url, expected in urls:
        self.assertEqual(swatcher.swatch_url(url), expected, msg=f"Using url {url}")
