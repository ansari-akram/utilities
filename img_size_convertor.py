from glob import glob                                                           
import cv2 
import os 

# Image path 
image_path = glob('A:\\yolofacedetetction\\YOLO-Annotation-Tool\\Images\\002\\*.jpg')

# Image directory 
directory = 'A:\\yolofacedetetction\\YOLO-Annotation-Tool\\Images\\003'

try:
    for j in image_path:
        print(j[54:])
        filename = j[54:]
        img = cv2.imread(filename)
        resize = cv2.resize(img, (640, 480))
        cv2.imwrite(filename, resize)
except:
    print('exception')
    
print('Successfully saved')
