import numpy as np
from sys import argv
from PIL import Image

thres = 128 if len(argv) < 3 else int(argv[2])

img = Image.open(argv[1])
gray = np.array(img.convert('L'))
gray = np.where(gray > thres, 255, 0)
grayi = (255 - gray).astype(np.uint8)
img = Image.fromarray(np.stack([gray, gray, gray, grayi], axis=2).astype(np.uint8))
img.save('binary_{}.png'.format(argv[1][:-4]))
