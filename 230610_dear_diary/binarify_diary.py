import numpy as np
from sys import argv
from PIL import Image

srcdir = 'caption/0_raw'
dstdir = 'caption/1_binary'
thres = 128 if len(argv) < 3 else int(argv[2])

img = Image.open('{}/diary_{}.png'.format(srcdir, argv[1]))
img = img.resize((img.size[0] * 6, img.size[1] * 6), Image.LANCZOS)
gray = np.array(img.convert('L'))
gray = np.where(gray > thres, 255, 0)
grayi = (255 - gray).astype(np.uint8)
img = Image.fromarray(np.stack([gray, gray, gray, grayi], axis=2).astype(np.uint8))
img.save('{}/binary_{}.png'.format(dstdir, argv[1]))
