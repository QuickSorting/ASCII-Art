import PIL, os, numpy as np
from PIL import Image, ImageOps
from skimage.io import imread

# choose which image to show
IMAGE_NAME = "sample_image_4.jpg"

# increase constants for better quality picture, decrease to fit on screen
MAX_WIDTH = 400
MAX_HEIGHT = 240

# open and resize image
image_file = Image.open(IMAGE_NAME).convert("RGB")
new_size = [image_file.size[0] * 3, image_file.size[1] * 2]
minimum_division = max(1, new_size[0] / MAX_WIDTH, new_size[1] / MAX_HEIGHT)
for i in range(2):
    new_size[i] = round(new_size[i] / minimum_division)
image_file = image_file.resize(new_size)

# turn image pixels into np array
image = np.array(image_file)

# create grayscale image
image_gray = np.empty([image.shape[0], image.shape[1]])
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        avg = 0.0
        for color_value in image[i][j]:
            avg += color_value / image.shape[2]
        image_gray[i][j] = avg

# an ascii scale, in which a bigger index indicates a brighter(bigger) character
ascii_scale = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

# convert every pixel into an ascii character
image_ascii = np.empty(image_gray.shape, dtype = "str")
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        idx = image_gray[i][j] / 256.0 * (len(ascii_scale) - 1)
        image_ascii[i][j] = str(ascii_scale[int(round(idx))])

# show final image
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        print(image_ascii[i][j], end = '')
    print()