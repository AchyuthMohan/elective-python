from images import Image
filename = "test.gif"
image = Image(filename)
threshold =128
print("Width: ",image.getWidth())
print("Height: ",image.getHeight())
for i in range(image.getWidth()):
    for j in range(image.getHeight()):
        r, g, b = image.getPixel(i, j)
        average = (r+g+b)//3
        if average >= threshold:
            image.setPixel(i, j, (255, 255, 255))
        else:
            image.setPixel(i, j, (0, 0, 0))
image.save('bw.gif')
image.draw()
