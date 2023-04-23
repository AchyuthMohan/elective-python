from PIL import Image, ImageFilter
img = Image.open("achyut.gif")
img = img.convert("RGB")
img = img.filter(ImageFilter.GaussianBlur(radius=5))
img.save("blurred.gif")
