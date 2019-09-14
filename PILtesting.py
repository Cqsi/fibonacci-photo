from PIL import Image
import os

size_100 = (100,100)
name = "square.png"
path = "C:\\Users\\Capsimir\\Desktop\\VisualStudio\\PythonProjects\\PIL\\"

image1 = Image.open(path + name)
fn, fext = os.path.splitext(path + name)

image1.thumbnail(size_100)
image1.save("{}_100{}".format(fn, fext))

width, height = image1.size
print(str(width) + " " + str(height))

#for f in os.listdir(path):
#    if f.endswith(".jpg"):
#        i = Image.open(path + f)
#        fn, fext = os.path.splitext(f)
        
#        print(fn)


#image1.show()