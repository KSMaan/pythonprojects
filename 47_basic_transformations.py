from PIL import Image

dx = Image.open("dx.jpg")
square_dx = dx.resize((250, 250))
flip_dx = dx.transpose(Image.FLIP_LEFT_RIGHT)
spin_dx = dx.transpose(Image.ROTATE_90)

dx.show()
square_dx.show()
flip_dx.show()
spin_dx.show()