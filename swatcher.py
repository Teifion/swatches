import urllib.request

# Swatches stored as a dictionary, key = name of swatch and value an RGB tuple of the colour
# RGB is stored as integers in the range of 0-255
swatches = {
  "black": (0, 0, 0),
  "grey": (50, 50, 150),
  "teal": (50, 50, 150),
  "navy": (0, 0, 100),
}

def _get_image(url):
  with urllib.request.urlopen(url) as f:
    return f.read()

def _swatch_image(image_source):
  swatch, distance = "", 0

  return swatch, distance

def swatch_url(url):
  """
  Main function of the swatcher library. Pass a URL and get back the swatch colour
  based on the image in the URL

  "https://pwintyimages.blob.core.windows.net/samples/stars/test-sample-black.png" -> "black"
  """
  image_source = _get_image(url)
  swatch_result, _distance = _swatch_image(image_source)

  return swatch_result
