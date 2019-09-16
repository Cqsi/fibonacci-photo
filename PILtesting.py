from PIL import Image
import os

name = "test_images\\square.png"
path = "C:\\Users\\Capsimir\\Desktop\\VisualStudio\\PythonProjects\\PIL\\"
fibonacci_photos = [(100, 100), (100, 100)]
fibonacci_limit = 5

for i in range(fibonacci_limit):
    fibonacci_photos.append((fibonacci_photos[i][0] + fibonacci_photos[i+1][0], fibonacci_photos[i][0] + fibonacci_photos[i+1][0]))

image1 = Image.open(path + name)
file_name, ext = os.path.splitext(name)

for i in range(len(fibonacci_photos)):
    #image1.resize(fibonacci_photos[i]).save((path + "converted\\" + "{}_" + str(fibonacci_photos[i][0]) + "{}").format(file_name, ext)
    image1.resize(fibonacci_photos[i]).save((path + "converted\\" + str(fibonacci_photos[i][0]) + "{}").format(ext))
    image1 = Image.open(path + name)

area_of_image = sum(i[0]*i[0] for i in fibonacci_photos)
new_image_size = (fibonacci_photos[-1][0], area_of_image//fibonacci_photos[-1][0])

new_image = Image.new("RGB", new_image_size)

# 1 = south
# 2 = east
# 3 = north
# 4 = west

direction = 1
x_point = 0
y_point = 0

for i in range(len(fibonacci_photos)-1, -1, -1):

    new_image.paste(Image.open(path + "converted\\" + str(fibonacci_photos[i][0]) + ".png"), (x_point, y_point))

    if direction == 1:
        y_point+=fibonacci_photos[i][0]
        direction+=1
    elif direction == 2:
        x_point+=fibonacci_photos[i][0]
        y_point+=fibonacci_photos[i][0]-fibonacci_photos[i-1][0]
        direction+=1
    elif direction == 3:
        x_point+=fibonacci_photos[i][0]-fibonacci_photos[i-1][0]
        y_point-=fibonacci_photos[i-1][0]
        direction+=1
    elif direction == 4:
        x_point-=fibonacci_photos[i-1][0]
        direction=1
    else:
        print("Something went wrong")

new_image.save(path + "fibonacci_photo\\" + "fibonacci.png")

for i in os.listdir(path + "converted\\"):
    os.remove(path + "converted\\" + i)
