import pickle
import numpy as np
import os.path
import base64
from PIL import Image
import sys

class Preprocessor:
	def preprocess(self,jpgtxt):
		data = jpgtxt.split(',')[-1]
		data = base64.b64decode(data.encode('ascii'))

		g = open("/home/l/Documents/github/test/temp.jpg", "wb")
		g.write(data)
		g.close()
		
		argv = '/home/l/Documents/github/test/temp.jpg'
		im = Image.open(argv).convert('L')
		width = float(im.size[0])
		height = float(im.size[1])
		# creates white canvas of 28x28 pixels
		newImage = Image.new('L', (28, 28), (0))

		if width > height:  # check which dimension is bigger
			# Width is bigger. Width becomes 20 pixels.
			# resize height according to ratio width
			nheight = int(round((20.0 / width * height), 0))
			if (nheight == 0):  # rare case but minimum is 1 pixel
				nheight = 1
				# resize and sharpen
			img = im.resize((20, nheight), Image.ANTIALIAS).filter(
				ImageFilter.SHARPEN)
			# calculate horizontal position
			wtop = int(round(((28 - nheight) / 2), 0))
			newImage.paste(img, (4, wtop))  # paste resized image on white canvas
		else:
			# Height is bigger. Heigth becomes 20 pixels.
			# resize width according to ratio height
			nwidth = int(round((20.0 / height * width), 0))
			if (nwidth == 0):  # rare case but minimum is 1 pixel
				nwidth = 1
				# resize and sharpen
			img = im.resize((nwidth, 20), Image.ANTIALIAS).filter(
				ImageFilter.SHARPEN)
			# caculate vertical pozition
			wleft = int(round(((28 - nwidth) / 2), 0))
			newImage.paste(img, (wleft, 4))  # paste resized image on white canvas
		img = cv2.cvtColor(newImage, cv2.COLOR_BGR2GRAY)
		img = np.asarray(img).reshape(-1)
		img = img/255.0
    	
		return img

	
