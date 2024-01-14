import cv2
import numpy
import math



def encode_word(word_encode):
    square = int(math.ceil(math.sqrt(len(word_encode))))

    image = []

    index = 0
    for y in range(square):

        image.append([])
        for _ in range(square):
            if index < len(word_encode):
                char_code = ord(word_encode[index])
                image[y].append([char_code])
            else:
                image[y].append([0,0,0])
            index += 1

    numpy_list = numpy.array(image)

    cv2.imwrite('image.png', numpy_list)
