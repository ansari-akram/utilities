# importing modeuls required
import os
from PIL import Image

# image path to convert
image_path = 'A:\\Tuition Photos'

# path to save the images
directory = 'A:\\dataset'

# code for appending the all jpg files in a list
files = []
for r, d, f in os.walk(image_path):
    for file in f:
        if '.jpg' in file:
            files.append(os.path.join(file))

# change your directory to the directory
os.chdir(directory)

# code for saving jpg in directory
for file in files:
    #print(file)
    img = Image.open(file)
    img = img.convert('RGB')
    temp = file[:-4]
    image_name = temp+'.jpg'
    img.save(image_name, quality=95)
    print('[INFO] converted ' + file + ' to ' + image_name)
