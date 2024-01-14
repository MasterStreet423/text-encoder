import cv2

def decode_image(image_path):
    img = cv2.imread(image_path)
    for i in img:
        for j in i:
            print(chr(j[0]), end="")
