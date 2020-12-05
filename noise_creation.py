from PIL import Image
import random

def createNoise(image, difference):
	#range is the possible increase in values
	newIm = Image.open(image)
	width, height = newIm.size
	#changedPixels holds the cooredinates of the pixels that will be changed
	changedPixels = []
	#every pixel has a 1/7 chance of being changed
	chance = 0
	for i in range(height):
		for j in range(width):
			chance = random.randint(0, 6)
			if chance == 0:
				changedPixels.append([j, i])
	#testing
	print(changedPixels[0])
	#changeTo holds the values of the new pixel values
	changeTo = []
	for pixels in changedPixels:
		pixelValue = newIm.getpixel(tuple(pixels))
		newPixelValue = []
		for i in range(3):
			tempValue = 0
			tempValue = pixelValue[i] + random.randint(0, difference)
			tempValue +- random.randint(0, difference)
			newPixelValue.append(tempValue)
		newPixelValue.append(pixelValue[3])
		changeTo.append(tuple(newPixelValue))
	#add the pixels
	for i in range(len(changedPixels)):
		newIm.putpixel((changedPixels[i]), changeTo[i])
	newIm.save(image)

image = str(input('insert image directory here > '))
difference = int(input('insert range of numbers here > '))
createNoise(image, difference)