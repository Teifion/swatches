import urllib.request
from io import BytesIO
from PIL import Image

# Swatches stored as a dictionary, key = name of swatch and value an RGB tuple of the colour
# RGB is stored as integers in the range of 0-255
_swatches = {
  "black": (0, 0, 0),
  "grey": (50, 50, 150),
  "teal": (50, 50, 150),
  "navy": (0, 0, 100),
}

# If the closest swatch is over this distance, we want to call attention to it
_maximum_distance = 150

def _get_image(url):
  # Opens the URL for the image and returns a fully fledged PIL image object
  with urllib.request.urlopen(url) as f:
    return Image.open(BytesIO(f.read()))

def _swatch_image(the_image):
  colour = _most_frequent_colour(the_image)
  distance, swatch = _find_closest_swatch(colour)

  # If we have too much of a distance, here is where we start calling attention to it
  if distance > _maximum_distance:
    return swatch, f"Error: Swatch distance exceeded. Got {distance} which is larger than {_maximum_distance}. Closest swatch was {swatch} with colour {colour}."

  return swatch, None

def _find_closest_swatch(colour):
  # Go through all swatches, find out which is closest
  closest_swatch = (99999, None)

  for swatch_name, swatch_colour in _swatches.items():
    distance = _colour_distance(swatch_colour, colour)

    if distance < closest_swatch[0]:
      closest_swatch = (distance, swatch_name)

  return closest_swatch

def _colour_distance(c1, c2):
  (r1, g1, b1) = c1
  (r2, g2, b2) = c2
  
  # Use abs so it doesn't matter which way the difference goes
  (rd, gd, bd) = (abs(r1 - r2), abs(g1 - g2), abs(b1 - b2))

  return rd + gd + bd

def _most_frequent_colour(the_image):
  # Go through all the colours, find out which is the most common
  w, h = the_image.size
  pixels = the_image.getcolors(w * h)

  most_frequent = (0, None)

  for count, colour in pixels:
    if count > most_frequent[0]:
      most_frequent = (count, colour)

  return most_frequent[1]

def swatch_url(url):
  """
  Main function of the swatcher library. Pass a URL and get back the swatch colour
  based on the image in the URL, also get back an error message (or None with no error)

  "https://pwintyimages.blob.core.windows.net/samples/stars/test-sample-black.png" -> "black"
  """
  the_image = _get_image(url)
  swatch_result, error = _swatch_image(the_image)

  # If the swatch colour and dominant colour are too far apart, this is where
  # we would go about logging it
  if error:
    pass

  return swatch_result
