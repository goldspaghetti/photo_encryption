#use ord() to get acii values from letters and chr() for the reverse
from PIL import Image
import argparse

def encrypt(image, message, newImDirect):
	numberList = []
	for letter in message:
		numberList.append(ord(letter))
	pixelValues = []
	newIm = Image.open(image)
	width, height = newIm.size
	pixelCount = 0
	for pixels_h in range(height):
		for pixels_w in range(0, width, 5):
			pixelValues.append(newIm.getpixel((pixels_w, pixels_h)))
			pixelCount += 1
			if pixelCount >= len(numberList):
				break
		else:
			continue
		break
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
	pixelCount = 0
	for pixels_h in range(height):
		for pixels_w in range(0, width, 5):
			newIm.putpixel((pixels_w, pixels_h), tuple(pixelReplace[pixelCount]))
			#random debug stuff
			print(str(pixelReplace[pixelCount][1]))
			pixelCount += 1
			if pixelCount >= len(pixelReplace):
				break
		else:
			continue
		break
	print('part 3 working')
	if newImDirect:
		newIm.save(newImDirect)
	else:
		newIm.save(image)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='decrypt or encrypt images')
	parser.add_argument('image', help='direct path to image file')
	parser.add_argument('message', help='message to insert')
	parser.add_argument("-i", "--newImage", help='new image directory')
	args = parser.parse_args()
encrypt(args.image, args.message, args.newImage)
