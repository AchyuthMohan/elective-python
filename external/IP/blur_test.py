from images import Image
def convert(image,radius=1):
    for x in range(image.getWidth()):
        for y in range(image.getHeight()):
            image.setPixel(x,y,gradient(x,y,radius,image))
    image.draw()
    image.save('blurred.gif')

def gradient(x,y,radius,image):
    r_total=0
    g_total=0
    b_total=0
    count=0
    for dx in range(-radius,radius+1):
        for dy in range(-radius,radius+1):
            nx=x+dx
            ny=y+dy
            if 0<=nx<radius and 0<=ny<radius:
                r,g,b=image.getPixel(nx,ny)
                r_total+=r
                g_total+=g
                b_total+=b
                count+=1
    r_avg=r_total//count
    g_avg=g_total//count
    b_avg=b_total//count
    return(r_avg,g_avg,b_avg)

image=Image("test.gif")
convert(image,3)