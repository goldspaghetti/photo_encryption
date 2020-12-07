from PIL import Image
import argparse
def decrypt(image, key):
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
	terminatingColor = 100
	message = ""
	count = 0
	while True:
		count += 1
		#currentNumber holds the corresponding value
		currentNumber = key
		while currentNumber % greatestPrime != count+1:
			currentNumber += key
		heightValue = 0
		widthValue = currentNumber
		while widthValue >= width:
			heightValue += 1
			widthValue -= width
		print('-------start of coordinates-------')
		print(widthValue)
		print(heightValue)
		pixelValue = newIm.getpixel((widthValue, heightValue))
		message += chr(pixelValue[0])
		if pixelValue[1] == terminatingColor:
			print('terminated \n')
			break
	print(message)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='decrypt images')
	parser.add_argument('image', help='direct path to image file')
	parser.add_argument('key', help='prime number encryption key', default=3, type=int)
	args = parser.parse_args()
decrypt(args.image, args.key)