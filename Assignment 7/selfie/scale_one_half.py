from PIL import Image
img = Image.open("achyut.gif")
width, height = img.size
new_width = width // 2
new_height = height // 2
img = img.resize((new_width, new_height))
img.save("scaled.gif")
