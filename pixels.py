from PIL import Image
import random


def main():
	image = getPixelsList()
	image_clone = image
	clusters = 2

	clusters_colors, clusters_positions = generatePopulation(image, clusters)

'''
	image_path: may have a parameter that is the path to the file we wanna open
	return: the return is n array lines of m pixels
'''

def getPixelsList(image_path=None):
	im = Image.open("torre.jpg")

	pixels = list(im.getdata())
	width, height = im.size
	return [pixels[i * width:(i + 1) * width] for i in xrange(height)]
	
def getPixelRandomly(image):
	return random.randrange(len(image)), random.randrange(len(image[1]))

def generatePopulation(image, clusters):
	population = []
	centroids = []
	for i in range(clusters):
		x, y = getPixelRandomly(image)
		centroid = image[x][y]
		population.append(centroid)
		centroids.append((x, y))

	print "clusters_colors: ", population, "\nclusters_positions: ", centroids
	return population, centroids

# Calculates euclidean distance between a data point and all the available cluster centroids.      
def euclidean_dist(image, centroids, clusters):
	smaller_distance = 500

	for pixel in image:
        # Find which centroid is the closest to the given data point.
		for centroid in centroids:
			r1, g1, b1 = pixel
			r2, g2, b2 = centroid

		color_distance = sqrt((r2-r1)^2+(g2-g1)^2+(b2-b1)^2)

		if color_distance < smaller_distance:
	 		smaller_distance = color_distance

    # If any cluster is empty then assign one point
    # from data set randomly so as to not have empty
    # clusters and 0 means.        
    #for cluster in clusters:
        #if not cluster:
            #cluster.append(data[np.random.randint(0, len(data), size=1)].flatten().tolist())

    #return clusters


if __name__ == "__main__":
	main()
