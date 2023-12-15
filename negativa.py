from PIL import Image

img =  Image.open('img/uefs.jpeg')

matriz_img = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        r = 255 - matriz_img[i, j][0]
        g = 255 - matriz_img[i, j][1]
        b = 255 - matriz_img[i, j][2]
        matriz_img[i, j] = (r, g, b)

img.save('img/uefs_inversa.jpeg')