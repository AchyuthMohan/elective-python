from PIL import Image, ImageDraw, ImageFilter

def draw_face_rectangles(image_path, faces):
    with Image.open('abhishek.gif') as img:
        img = img.convert('P', palette=Image.Palette.ADAPTIVE, colors=256)
        draw = ImageDraw.Draw(img)
        for face in faces:
            draw.rectangle(face, outline='black')
        img.save("face_rectangles.gif")
        img.show()
