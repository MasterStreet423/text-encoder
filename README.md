# Encode-Decode Image Repository

Este repositorio contiene dos archivos Python que te permitirán codificar y decodificar texto en una imagen utilizando la biblioteca OpenCV (cv2) y NumPy. La idea principal es convertir un mensaje de texto en una imagen y luego recuperar el mensaje original a partir de la imagen generada.
Archivos en el Repositorio
### encode-image.py

Este archivo contiene una función llamada encode_word que toma una cadena de texto como entrada y crea una imagen cuadrada con cada píxel representando un carácter de la cadena. Si la cadena es más larga que el área de la imagen, la función extiende la imagen según sea necesario. La imagen resultante se guarda en un archivo llamado 'image.png'.

```python

import cv2
import numpy
import math

def encode_word(word_encode):
    # ... (código para generar la imagen)
    cv2.imwrite('image.png', numpy_list)
```
### decode-image.py

Este archivo contiene una función llamada decode_image que toma la ruta de una imagen como entrada y decodifica la imagen para recuperar el mensaje original. Luego, imprime el mensaje en la consola.

```python

import cv2

def decode_image(image_path):
    # ... (código para decodificar la imagen)
    for i in img:
        for j in i:
            print(chr(j[0]), end="")
```
## Uso del Repositorio

Clona el repositorio a tu máquina local:

```bash

git clone https://github.com/tu-usuario/text-encoder.git
cd text-encoder
```

Modifica el archivo encode-image.py para incluir tu propia cadena de texto:

```python

encode_word("Tu mensaje secreto aquí")
```

Ejecuta el script encode-image.py:

```bash

python encode-image.py
```
Esto generará la imagen codificada 'image.png' en el mismo directorio.

Para decodificar el mensaje, modifica el archivo decode-image.py con la ruta correcta de la imagen generada:

```python

decode_image("image.png")
```
Ejecuta el script decode-image.py:

```bash

    python decode-image.py

    Esto imprimirá el mensaje original en la consola.
```
¡Disfruta explorando este simple pero intrigante sistema de codificación de imágenes! Siéntete libre de personalizar y mejorar los scripts según tus necesidades.
