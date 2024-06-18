import cv2
import os

detect_human = cv2.HOGDescriptor()
detect_human.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

file_path = os.path.abspath('image6.jpeg')
print(file_path)

image = cv2.imread(file_path) 

humans, _ = detect_human.detectMultiScale(image, winStride=(10, 10),
                                          padding=(32, 32), scale=1.1)

if len(humans) > 0:
    print("Human image.")
else:
    print("Not a Human image.")
