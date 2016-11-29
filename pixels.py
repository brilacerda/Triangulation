import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy
from math import sqrt, floor
numpy.seterr(over='ignore')

fitness = []

def main():
	global fitness
	image = getPixelsList()
	img_clone  = []
	clusters = 2

	# Initializing the fitness
	for i in range(clusters):
		fitness.append(0)

	centroid_colors, centroid_array_positions = generatePopulation(image, clusters)
	img_clone = fitness_n_color_distance(image, centroid_colors, len(image))
	plotImage(img_clone)
	
	# image_clone = formatToImage(img_clone, len(image[0]), len(image))
	for i in range(30):
		print i + 1, " iteration"

		for j in range(int (floor(clusters*0.4))+1):
			print "# Recombination ", i
			if random.random() <= 0.9:
				centroid_colors = recombine(img_clone, clusters, centroid_colors)
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
	r1, g1, b1 = r1g1b1
	r2g2b2 = image[c][d]
	r2, g2, b2 = r2g2b2
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

def formatToImage(image, column, line):
	aux = []
	img2 = []
	pointer = 0

	for i in range(column):
		for j in range(line):
			aux.append(image[pointer])
			pointer = pointer + 1

		img2.append(aux)
		aux = []

	return img2

def calculate_fitness(fitness_data):
	global fitness

	fitness[fitness_data[1]] = fitness[fitness_data[1]] + fitness_data[0]


# Calculates euclidean distance between a data point and all the available cluster centroids.      
def fitness_n_color_distance(image, centroids, width):
	cluster_debut = []
	image_classification = []
	quantized_image = []

	# Check if all clusters have at least one pixel associated
	for i in centroids:
		cluster_debut.append(False)

	for height in range(len(image)):
		aux_img_class = []
		aux_quatiz_img = []
		for width in range(len(image[0])):
			smaller_distance = (500, -1)

			'''
				Classify in clusters
			'''
	        # Find which centroid is the closest to the given data point.
			centroid_array_position = 0
			
			for centroid in centroids:
				r1, g1, b1 = image[height][width]
				r2, g2, b2 = centroid

				# code reuse
				r = r2-r1
				g = g2-g1
				b = b2-b1

				color_distance = abs(int (r)^2+ int (g)^2+ int (b)^2)
				color_distance = sqrt(color_distance)
				'''
					Calculate the fitness and the color distance
				'''

				if color_distance < smaller_distance[0]:
			 		smaller_distance = (int (r)+ int (g)+ int (b), centroid_array_position)

			 	centroid_array_position = centroid_array_position +1

			calculate_fitness(smaller_distance)

			if not cluster_debut[smaller_distance[1]]:
				cluster_debut[smaller_distance[1]] = True

		#The next 4 lines of code are necessary to format the proper image matrix

			# Saves all the distances and the the quantized image matrix takes the color of 
			# the centroid with the smaller distance between the pixel and the centroid
			aux_img_class.append(smaller_distance)
			aux_quatiz_img.append(centroids[smaller_distance[1]])

		image_classification.append(aux_img_class)
		quantized_image.append(aux_quatiz_img)

    # If any cluster is empty then assign one point from data set randomly so as to not have empty
    # clusters and 0 means.        
	array_position = 0
	for debut in cluster_debut:
		if not debut:
			x, y = getPixelRandomly(image)
			r1, g1, b1 = image[x][y]
			r2, g2, b2 = centroids[array_position]
			color_distance = sqrt(abs((r2-r1)^2+(g2-g1)^2+(b2-b1)^2))
			image_classification[x][y]
		array_position = array_position +1

	return quantized_image


if __name__ == "__main__":
	main()
