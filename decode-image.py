import cv2

img = cv2.imread('./image.png')

for i in img:
    for j in i:
        print(chr(j[0]), end="")
