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
      self.assertEqual(swatcher.swatch_url(url), expected, msg=f"Testing url {url}")

  def test_find_closest_swatch(self):
    colours = [
      ()
    ]

    for colour, expected in colours:
      self.assertEqual(swatcher._find_closest_swatch(colour), expected, msg=f"Testing colour {colour}")

  def test_colour_distance(self):
    colours = [
      ()
    ]

    for c1, c2, expected in colours:
      self.assertEqual(swatcher._colour_distance(c1, c2), expected, msg=f"Testing colours {c1} and {c2}")
