import numpy as np
from PIL import Image
from os import listdir
from sys import argv

srcdir = 'caption/3_lines'
dstdir = 'caption/4_lines_rect'

for file in listdir(srcdir):

	if len(argv) > 1 and file != argv[1]:
		continue

	path = '{}/{}'.format(srcdir, file)
	img = Image.open(path)

	cpart = False
	if file.startswith('va'):
		file = file.replace('va', 'vc')
	elif file.startswith('vb'):
		file = file.replace('vb', 'vd')
	elif file.startswith('vc'):
		file = file.replace('vc', 'va')
	elif file.startswith('vd'):
		file = file.replace('vd', 'vb')
	if file.startswith('c') and file.endswith('a.png'):
		file = file.replace('a', 'x')
		size = 4
		cpart = True
	if file.startswith('c') and file.endswith('b.png'):
		file = file.replace('b', 'y')
		size = 10
		cpart = True
	if file.startswith('c8'):
		size = 5
	if file.startswith('v'):
		size = 14
	if (file.endswith('x.png') or file.endswith('y.png')) and not cpart:
		size = 6
	if '_' in file:
		size = int(file[:-4].split('_')[1])

	w = size * 200
	h = img.size[1] * w // img.size[0]
	file = file[:-4].split('_')[0]

	img = img.resize((w, h), Image.LANCZOS)
	gray = np.array(img.convert('L')).astype(np.uint8)
	gray = np.where(gray > 128, 255, 0)
	grayi = (255 - gray).astype(np.uint8)

	img = Image.fromarray(np.stack([gray, gray, gray, grayi], axis=2).astype(np.uint8))
	canvas = Image.new('RGBA', (w, 300), (255, 255, 255, 0))
	canvas.paste(img, (0, (canvas.size[1] - img.size[1]) // 2))
	canvas.save('{}/{}_r.png'.format(dstdir, file))
