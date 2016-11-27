from PIL import Image
import random


def main():
	image = getPixelsList()
	image_clone = image
	clusters = 2
	population = []

	for i in range(clusters):
		x, y = getPixelRandomly(image)
		print x, y
		centroid = image[x][y]
		population.append(centroid)

	print population

'''
	image_path: may have a parameter that is the path to the file we wanna open
	return: the return is n array lines of m pixels
'''

def getPixelsList(image_path=None):
	im = Image.open("torreMalakoff.jpg")

	pixels = list(im.getdata())
	width, height = im.size
	return [pixels[i * width:(i + 1) * width] for i in xrange(height)]
	
def getPixelRandomly(image):
	return random.randrange(len(image)), random.randrange(len(image[1]))


if __name__ == "__main__":
	main()
