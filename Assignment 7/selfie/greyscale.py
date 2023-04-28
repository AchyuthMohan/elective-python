from PIL import Image
img = Image.open("abhishek.gif")
gray_img = img.convert('L')
gray_img.save("grey.gif")