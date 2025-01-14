# importing PIL.Image library and os library
from PIL import Image 
import os
import random

# Deletes old created images if they exist
if os.path.exists("newImage.jpg"):
  os.remove("newImage.jpg")

change = input("How much do you want your image to change: 1, 2 or 3? ")

# Prints two blank lines to start our program output
print("\n\n")

# Opens image - Local File in repl.it
img = Image.open('image.jpg')

# Rescale image size down, if needed
width = img.width
height = img.height
mwidth = width // 1000
mheight = height // 1000
if mwidth > mheight:
  scale = mwidth
else:
  scale = mheight
if scale != 0:
  img = img.resize( (width // scale, height // scale) )

########################
#        Filter        #
########################
def newFilter():
  # Starts at the first pixel in the image
  location = 0
  # Continues until it has looped through all pixels
  while location < len(new_pixels):

    if change =="1":
       rand = random.randint(1, 10)
    elif change == "2":
      rand = random.randint(11, 20)
    elif change == "3":
      rand = random.randint(21, 30)
    else:
      rand = 0

    if location < 30:
      newp = new_pixels[location + rand ]
    else:
      newp = new_pixels[location - rand ]
    nr = newp[0]
    ng = newp[1]
    nb = newp[2]
    # Gets the current color of the pixel at location
    p = new_pixels[location]
    # Splits color into red, green and blue components
    r = p[0]
    g = p[1]
    b = p[2]
    # Perform pixel manipulation and stores results
    # to a new red, green and blue components
    newr = int((r + nr)/2)
    newg = int((g + ng)/2)
    newb = int((b + nb)/2)
    # Assign new red, green and blue components to pixel
    # at that specific location
    new_pixels[location] = (newr, newg, newb)
    # Changes the location to the next pixel in array
    location = location + 1
  # Creates a new image, the same size as the original 
  # using RGB value format
  newImage = Image.new("RGB", img.size)
  # Assigns the pixel values to newImage
  newImage.putdata(new_pixels)
  # Saves the new image file
  newImage.save("newImage.jpg")

# Creates an ImageCore Object from original image
pixels = img.getdata()
# Creates empty array to hold new pixel values
new_pixels = []
# For every pixel from our original image, it saves
# a copy of that pixel to our new_pixels array
for p in pixels:
  new_pixels.append(p)

# Calls the newFilter function to create the image
newFilter()
