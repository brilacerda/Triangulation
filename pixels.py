from PIL import Image

def getPixelsList(image):
	im = Image.open(image)

	pixels = list(im.getdata())
	width, height = im.size
	pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
	print pixels