from PIL import Image
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy
from math import sqrt, floor
numpy.seterr(over='ignore')

fitness = []

def main():
	image = getPixelsList()
	img_clone  = image
	clusters = 2

	centroid_colors, centroid_array_positions = generatePopulation(image, clusters)
	img_clone = fitness_n_color_distance(image, centroid_colors, len(image))
	plotImage(img_clone)

	for i in range(30):
		print i + 1, " iteration"

		for j in range(int (floor(clusters*0.4))):
			print "# Recombination ", i
			if random.random() <= 0.9:
				centroid_colors = recombine(img_clone.tolist(), clusters, centroid_colors)
		if random.random() <= 0.3:
			print "# Mutation"
			centroid_colors = mutate(img_clone, clusters, centroid_colors)

		img_clone = fitness_n_color_distance(image, centroid_colors, len(image))
		plotImage(img_clone)

'''
	image_path: may have a parameter that is the path to the file we wanna open
	return: the return is n array lines of m pixels
'''
def getPixelsList(image_path=None):
	return mpimg.imread('torre.jpg')
	
def plotImage(image):
		imgplot = plt.imshow(image)
		plt.show()

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

def recombine(image, k, centroid_colors):
	a, b = getPixelRandomly(image)
	c, d = getPixelRandomly(image)
	
	r1g1b1 = image[a][b]
	r1, g1, b1 = r1g1b1.tolist()
	r2g2b2 = image[c][d]
	r2, g2, b2 = r2g2b2.tolist()
	child = random.randrange(k)
	centroid_colors[child] = ((r2-r1)/2, (g2-g1)/2, (b2-b1)/2)
	return centroid_colors

def mutate(image, k, centroid_colors):
	x, y = getPixelRandomly(image)
	print x, y
	rgb = image[x][y]
	print rgb

	child = random.randrange(k)
	print child
	centroid_colors[child] = (rgb[0], rgb[1], rgb[2])
	return centroid_colors

# Calculates euclidean distance between a data point and all the available cluster centroids.      
def fitness_n_color_distance(image, centroids, width):
	global fitness
	cluster_debut = []
	image_classification = []
	quantized_image = []
	archive = open('quantized_image', 'w')

	image = numpy.reshape(image, (-1, 3))
	# Check if all clusters have at least one pixel associated
	for i in centroids:
		cluster_debut.append(False)

	for pixel in image:
		smaller_distance = (500, -1)

		'''
			Classify in clusters
		'''

        # Find which centroid is the closest to the given data point.
		centroid_array_position = 0
		
		for centroid in centroids:
			r1, g1, b1 = pixel
			r2, g2, b2 = centroid
			#print r1, g1, b1, '--', r2, g2, b2

			# code reuse
			r = abs(r2-r1)
			g = abs(g2-g1)
			b = abs(b2-b1)

			fitness = int (r)^2+ int (g)^2+ int (b)^2
			'''
				Calculate the fitness and the color distance
			'''

			color_distance = sqrt(fitness)

			if color_distance < smaller_distance[0]:
		 		smaller_distance= (fitness, centroid_array_position)

		 	centroid_array_position = centroid_array_position +1

		 # Saves all the distances and the 
		image_classification.append(smaller_distance)
		# the quantized image matrix takes the color of the centroid with the smaller
		# distance between the pixel and the centroid
		quantized_image.append(centroids[smaller_distance[1]])

		if not cluster_debut[smaller_distance[1]]:
			cluster_debut[smaller_distance[1]] = True

	image_classification = numpy.reshape(image_classification, (width, -1))
	quantized_image = numpy.reshape(quantized_image, (width, -1))

    # If any cluster is empty then assign one point from data set randomly so as to not have empty
    # clusters and 0 means.        
	array_position = 0
	for debut in cluster_debut:
		if not debut:
			x, y = getPixelRandomly()
			r1, g1, b1 = image[x][y]
			r2, g2, b2 = centroids[array_position]
			color_distance = sqrt((r2-r1)^2+(g2-g1)^2+(b2-b1)^2)
			image_classification[x][y]
		array_position = array_position +1

	return quantized_image


if __name__ == "__main__":
	main()
