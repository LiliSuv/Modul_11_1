import numpy as np
from PIL import Image
import time


a = np.array([[1, 2,17], [5, 6,2], [91, 10,3]])
print(f'Количество элементов массива: {a.size}')
print(f'Нарезка массива: {a[1:3]}')
print( f'Максимум: {a.max()}')
print( f'Сумма: {a.sum()}')
a=np.array([[1, 2], [5, 6]])
b=np.array([[3, 7], [9, 4]])
print( f'Умножение массивов: {a*b}')
print ("**"*20,'\n')
time.sleep (5)
g= Image.open("1.jpg")
print( f'Первоначальный размер изображения: {g.size}')
size = (200, 400)
with Image.open("1.jpg") as im:
    im.thumbnail (size)
    im.save ("2.jpg")
g= Image.open("2.jpg")
print(f"Размер измененного изображения:{g.size}" )
time.sleep (5)
with Image.open("1.jpg") as im:
    s = im.convert("L")
    r = im.transpose (Image.Transpose.ROTATE_270)
    box = (0, 0, 120, 120)
    region = im.crop (box)
g.show()
time.sleep (5)
s.show ()
time.sleep (5)
r.show ()
time.sleep (5)
region.show ()
time.sleep (5)
with Image.open("1.jpg") as im:
    im.rotate(45).show()
    time.sleep (5)
    rgb2xyz = (
        0.99, 0, 0.23, 0.5,
        0.1, 0.160, 0.99, 0.96,
        0.34, 0.95, 135, 0)
    im.convert ("RGB", rgb2xyz).show()

