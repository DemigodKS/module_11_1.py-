from PIL import Image
from PIL import ImageFilter
import time
#Библиотека Pillow (PIl) позволяет работать с изображением
#ниже пример по небольшой части возможностей библиотеки
filename = "buildings.jpg"
with Image.open(filename) as img:
    img.show()
time.sleep(3)
print(type(img))
print(isinstance(img, Image.Image))
print(img.format)
print(img.size)
print(img.mode)

#переворачиваем изображение
converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)
converted_img.show()
time.sleep(3)
#поворачиваем изображение и вписываем его в границы
rotated_img = img.rotate(45, expand=True)
rotated_img.show()
time.sleep(3)
#форматируем в черно-белую
blackAndWhite = img.convert("L")
blackAndWhite.save("black.jpg")
filename1 = "black.jpg"
#размытие фотки
img.filter(ImageFilter.BoxBlur(5)).show()
with Image.open(filename1) as img1:
    time.sleep(3)
    img1.show()

