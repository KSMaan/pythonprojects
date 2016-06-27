from PIL import Image
from PIL import ImageFilter
dx = Image.open("dx.jpg")
black_white = dx.convert("L")
black_white.show()

austin316 = Image.open("austin316.jpg")
blur = austin316.filter(ImageFilter.BLUR)
detail = austin316.filter(ImageFilter.DETAIL)
edges = austin316.filter(ImageFilter.FIND_EDGES)

blur.show()
detail.show()
edges.show()

