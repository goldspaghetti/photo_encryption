#use ord() to get acii values from letters and chr() for the reverse
from PIL import Image
import argparse

def encrypt(image, message, key, newImDirect):
	#generate prime numbers
	numberList = []
	for letter in message:
		numberList.append(ord(letter))
	newIm = Image.open(image)
	width, height = newIm.size

	totalPixels = width * height
	primeNumbers = [1, 2]
	count = 2
	print(totalPixels)
	print(key)
	while primeNumbers[-1] * key <= totalPixels:
		count += 1
		for numbers in range(len(primeNumbers) -1):
			if count % primeNumbers[numbers+1] == 0:
				break
			else:
				if numbers + 2 == len(primeNumbers):
					primeNumbers.append(count)
	greatestPrime = primeNumbers[-2]
	print(greatestPrime)
	primeValues = []
	for i in range(len(numberList)):
		currentNumber = key
		while currentNumber % greatestPrime != i+1:
			currentNumber += key
		primeValues.append(currentNumber)
		print('---------------')
		print('out of while')
		print(currentNumber)
	print(primeValues)

	pixelCoordinates = []
	for values in primeValues:
		heightValue = 0
		widthValue = values
		while widthValue >= width:
			heightValue += 1
			widthValue -= width
		print('-------start of coordinates-------')
		print(widthValue)
		print(heightValue)
		pixelCoordinates.append((widthValue, heightValue))

	pixelValues = []
	for pixels in pixelCoordinates:
		pixelValues.append(newIm.getpixel(pixels))
		print('one worked')

	print(str(len(numberList)))
	print(str(len(pixelValues)))
	print('part 1 working')
	pixelReplace = []
	for pixels in pixelValues:
		pixelReplace.append(list(pixels))
	terminatingColor = 100 #blue
	for i in range(len(pixelReplace)):
		pixelReplace[i][0] = numberList[i]
		if pixelReplace[i][1] == terminatingColor:
			pixelReplace[i][1] = terminatingColor - 1
		if i == len(pixelReplace) -1:
			pixelReplace[i][1] = terminatingColor
			print('terminated added\n')
	#add a terminating pixel
	print('part 2 working')
	print(str(len(pixelReplace)))
	for pixels in range(len(pixelCoordinates)):
		newIm.putpixel(tuple(pixelCoordinates[pixels]), tuple(pixelReplace[pixels]))
	print('part 3 working')
	if newImDirect:
		newIm.save(newImDirect)
	else:
		newIm.save(image)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='encrypt messages into images')
	parser.add_argument('image', help='direct path to image file')
	parser.add_argument('message', help='message to insert')
	parser.add_argument("-k", "--key", help='encryption key', default=3, type=int)
	parser.add_argument("-i", "--newImage", help='new image directory')
	args = parser.parse_args()
encrypt(args.image, args.message, args.key, args.newImage)
