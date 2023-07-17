from images import Image
image=Image('test.gif')

for x in range(image.getWidth()):
    for y in range(image.getHeight()):
        (r,g,b)=image.getPixel(x,y)
        avg=(r+g+b)//3
        image.setPixel(x,y,(avg,avg,avg))
image.save('grayscale.gif')
image.draw()
