from PIL import Image
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

fitness = []

def main():
	image = getPixelsList()
	image_clone = image
	clusters = 2

	centroid_colors, centroid_array_positions = generatePopulation(image, clusters)


	imgplot = plt.imshow(image)
	plt.show()
'''
	image_path: may have a parameter that is the path to the file we wanna open
	return: the return is n array lines of m pixels
'''
def getPixelsList(image_path=None):
	return mpimg.imread('torre.jpg')
	
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
def euclidean_dist(image, centroids):
	cluster_debut = []
	image_classification = []

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

			# code reuse
			r = r2-r1
			g = g2-g1
			b = b2-b1

			color_distance = sqrt(r^2+ g^2+ b^2)

			if color_distance < smaller_distance[0]:
		 		smaller_distance[0] = color_distance
		 		smaller_distance[1] = centroid_array_position

		 	centroid_array_position = centroid_array_position +1

		 # Saves all the distances and the 
		image_classification.append(smaller_distance)

		if not cluster_debut[smaller_distance[1]]:
			cluster_debut[smaller_distance[1]] = True

	image_classification = numpy.reshape(image_classification, (len(image), -1))

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
	
	'''
		Calculate the fitness
	'''
	
	global fitness
	for i in range(len(image_classification)):
		if image_classification[i][1] == 
		


    #return clusters


if __name__ == "__main__":
	main()
