from PIL import Image

apple = Image.open("apple.jpg")
r, g, b = apple.split()

new_img = Image.merge("RGB", (r, g, b))

#new_img.show()

new_img2 = Image.merge("RGB", (b, g, r))

#new_img2.show()

greenm = Image.open("greenm.jpg")

r1, g1, b1 = apple.split()
r2, g2, b2 = greenm.split()

new_img3 = Image.merge("RGB", (r2, g1, b2))

new_img3.show()