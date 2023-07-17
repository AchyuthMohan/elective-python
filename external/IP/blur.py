from images import Image

def apply_gaussian_blur(image, radius=1):
    width = image.getWidth()
    height = image.getHeight()
    blurred_image = Image(width, height)
    for x in range(width):
        for y in range(height):
            blurred_pixel = calculate_blurred_pixel(image, x, y, radius)
            blurred_image.setPixel(x, y, blurred_pixel)
    return blurred_image


def calculate_blurred_pixel(image, x, y, radius):
    r_total, g_total, b_total = 0, 0, 0
    count = 0
    for dx in range(-radius, radius+1):
        for dy in range(-radius, radius+1):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < image.getWidth() and 0 <= ny < image.getHeight():
                r, g, b = image.getPixel(nx, ny)
                r_total += r
                g_total += g
                b_total += b
                count += 1
    r_average = r_total // count
    g_average = g_total // count
    b_average = b_total // count

    return (r_average, g_average, b_average)


image_file = "bw.gif"
image = Image(image_file)
blurred_image = apply_gaussian_blur(image, radius=3)
output_file = "output_image_blurred.gif"
blurred_image.save(output_file)
image.draw()
blurred_image.draw()
