from PIL import Image, ImageFilter


i1 = Image.open('1.jpg')

i2 = i1.filter(ImageFilter.CONTOUR)

i2.save('3.jpg')

i3 = i1.filter(ImageFilter.BLUR)

i3.save('4.jpg')


# i2.show()
i3.show()