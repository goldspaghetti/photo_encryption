from PIL import Image
def decrypt(image):
	newIm = Image.open(image)
	width, height = newIm.size
	pixelList = []
	terminatingColor = 100
	for pixels_h in range(height):
		for pixels_w in range(0, width, 5):
			pixelList.append(newIm.getpixel((pixels_w, pixels_h)))
			if newIm.getpixel((pixels_w, pixels_h))[1] == terminatingColor:
				print('terminated \n')
				break
		else:
			print('no stop\n')
			continue
		break
	pixelValues = []
	for pixels in range(len(pixelList)):
		pixelValues.append(pixelList[pixels][0])
	letterList = []
	for pixels in pixelValues:
		letterList.append(chr(pixels))
	message = ""
	for letters in letterList:
		message += letters
	return message

image = str(input("enter image directory here> "))
message = decrypt(image)
print(message)