import os
from PIL import Image
image_path = 'A:\\Tuition Photos'
directory = 'A:\\dataset'

files = []
for r, d, f in os.walk(image_path):
    for file in f:
        if '.jpg' in file:
            files.append(os.path.join(file))

os.chdir('A:\\dataset')
count = 0
for file in files:
    print(file)
    img = Image.open(file)
    img = img.convert('RGB')
    image_name = file+'.jpg'
    img.save(image_name, quality=95)
