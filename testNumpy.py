#!/usr/local/bin/python3

import numpy as np

black, white, transparent = 0, 1, 2
height, width = 2,2
marsData = "0222112222120000"

class SpaceImage:
	
	def __init__(self, imageData, height, width):
		self.height = height
		self.width = width
		self.layerSize = height * width
		self.layers = int(len(imageData) / (width * height))
		self.image = self.__createMatrix(imageData)
		
	def __createMatrix(self, data):
		startingArray = [int(x) for x in data]	
		imageArray = np.array(startingArray)
		imageArray = imageArray.reshape((self.layers, self.height, self.width))
		return imageArray


def computeOutput(image):
	reverseImage = image[::-1]
	layers, height, width = image.shape

	returnImage = reverseImage[0].reshape(height * width,)

	for i in range(1,layers):
		maskImage = reverseImage[i].reshape(height * width,)
		newArray = np.array([], dtype=np.int64)
		for k in range(len(maskImage)):
			if int(maskImage[k]) in [black, white]:
				newArray = np.append(newArray, int(maskImage[k]))
			else:
				newArray = np.append(newArray, int(returnImage[k]))
		returnImage = newArray
	returnImage = returnImage.reshape(height, width)
	return returnImage

def printImage(image):
	chars = [32,9632]
	for line in image:
		for pixel in line:
			print(chr(chars[pixel]), end = '')
		print()
	

marsImage = SpaceImage(marsData, height, width)
# print(marsImage.image)
output=computeOutput(marsImage.image)
printImage(output)