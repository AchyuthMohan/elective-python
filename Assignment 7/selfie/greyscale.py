from PIL import Image
img = Image.open("achyut.gif")
gray_img = img.convert('L')
gray_img.save("grey.gif")
