from PIL import Image

dx = Image.open("dx.jpg")

print(dx.mode)
r, g, b = dx.split()

r.show()
g.show()
b.show()