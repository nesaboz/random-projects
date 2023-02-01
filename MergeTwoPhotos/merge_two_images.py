# import PIL module
from PIL import Image

# Front Image
filename = 'mute.png'


# Back Image
filename1 = 'black_t_shirt.jpeg'

# Open Front Image
frontImage = Image.open(filename)

# Open Background Image
background = Image.open(filename1)

# # Size of the image in pixels (size of original image)
# # (This is not mandatory)
# width, height = frontImage.size
# # Setting the points for cropped image
# left = 4
# top = height / 5
# right = 154
# bottom = 3 * height / 5
#
# # Cropped image of above dimension
# # (It will not change original image)
# im1 = im.crop((left, top, right, bottom))
# newsize = (300, 300)
# im1 = im1.resize(newsize)
# # Shows the image in image viewer
# im1.show()

frontImage = frontImage.convert("RGBA")
background = background.convert("RGBA")

width = (background.width - frontImage.width) // 2
height = (background.height - frontImage.height) // 2

background.paste(frontImage, (width, height), frontImage)

# Save this image
background.save("new.png", format="png")
