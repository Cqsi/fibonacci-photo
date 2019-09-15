from PIL import Image
import os

name = "square.png"
path = "C:\\Users\\Capsimir\\Desktop\\VisualStudio\\PythonProjects\\PIL\\"
fibonacci_photos = [(100, 100), (100, 100)]
fibonacci_limit = 4

for i in range(fibonacci_limit):
    fibonacci_photos.append((fibonacci_photos[i][0] + fibonacci_photos[i+1][0], fibonacci_photos[i][0] + fibonacci_photos[i+1][0]))

image1 = Image.open(path + name)
file_name, ext = os.path.splitext(name)

for i in range(len(fibonacci_photos)):
    image1.resize(fibonacci_photos[i]).save((path + "converted\\" + "{}_" + str(fibonacci_photos[i][0]) + "{}").format(file_name, ext))
    image1 = Image.open(path + name)

area_of_image = sum(i[0]*i[0] for i in fibonacci_photos)
new_image_size = (fibonacci_photos[-1][0], area_of_image/fibonacci_photos[-1][0])