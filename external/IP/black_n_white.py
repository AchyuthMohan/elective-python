from PIL import Image
image=Image.open('test.gif')
gs=image.convert('L')
# bw=gs.convert('1')
bw=gs.point(lambda pixel:0 if pixel<128 else 255 ,'1')
bw.show()