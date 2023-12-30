import cv2
import numpy
import math

word_encode = ""

with open('text.txt', 'r') as f:
    word_encode = f.read()

#obtengo el cuadrado cercano mas perfecto

square = int(math.ceil(math.sqrt(len(word_encode))))

image = []

index = 0
for y in range(square):
    image.append([])
    for x in range(square):
        if index < len(word_encode):
            ascii_code = ord(word_encode[index])
            #add array color [ascii,ascii,ascii]
            image[y].append([ascii_code,ascii_code,ascii_code])
        else:
            image[y].append([0,0,0])
        index += 1

numpy_list = numpy.array(image)

cv2.imwrite('image.png', numpy_list)
