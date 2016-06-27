from PIL import Image

img = Image.open("therock.jpg")
area = (100,100, 400, 400)
cropped_img = img.crop(area)

img.show()
cropped_img.show()