from images import Image
filename = "abhishek.gif"
image = Image(filename)
threshold = 128
for x in range(image.getWidth()):
    for y in range(image.getHeight()):
        r, g, b = image.getPixel(x, y)
        average = (r + g + b) // 3
        if average >= threshold:
            image.setPixel(x, y, (255, 255, 255))  
        else:
            image.setPixel(x, y, (0, 0, 0))  

image.draw()
