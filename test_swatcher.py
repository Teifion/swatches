import swatcher
import unittest

class SwatcherMethods(unittest.TestCase):
  def ttest_known_urls(self):
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
      # Exact matches
      ((0, 0, 0), "black"),
      ((50, 50, 50), "grey"),
      ((0, 100, 100), "teal"),
      ((0, 0, 100), "navy"),

      # Close matches
      ((20, 20, 20), "black"),
      ((40, 40, 40), "grey"),
      ((20, 120, 80), "teal"),
      ((20, 20, 80), "navy"),

      # Distance match, we could also use these values to test swatch distance failures
      ((20, 9999, 80), "teal"),
      ((20, 20, 9999), "navy"),
    ]

    for colour, expected in colours:
      _, found = swatcher._find_closest_swatch(colour)
      self.assertEqual(found, expected, msg=f"Testing colour {colour}")

  def test_colour_distance(self):
    colours = [
      # Test one direction
      ((0, 0, 0), (255, 255, 255), 765),
      ((0, 0, 0), (255, 0, 0), 255),
      ((0, 0, 0), (0, 255, 0), 255),
      ((0, 0, 0), (0, 0, 255), 255),
      
      # Test the other direction
      ((255, 255, 255), (0, 0, 0), 765),
      ((255, 0, 0), (0, 0, 0), 255),
      ((0, 255, 0), (0, 0, 0), 255),
      ((0, 0, 255), (0, 0, 0), 255),
    ]

    for c1, c2, expected in colours:
      self.assertEqual(swatcher._colour_distance(c1, c2), expected, msg=f"Testing colours {c1} and {c2}")
