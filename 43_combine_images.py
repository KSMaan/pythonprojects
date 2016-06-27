from PIL import Image

kaneandundertaker = Image.open("kaneandundertaker.jpg")
dx = Image.open("dx.jpg")

area = (0, 0, 602, 352)
kaneandundertaker.paste(dx, area)
kaneandundertaker.show()
