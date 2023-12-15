from PIL import Image

img =  Image.open('img/uefs.jpeg')

matriz_img = img.load()

gamma = float(input("Digite a intensidade da transformação gama: "))

for i in range(img.size[0]):
    for j in range(img.size[1]):
        r = int((matriz_img[i, j][0]/255) ** gamma * 255) 
        g = int((matriz_img[i, j][1]/255) ** gamma * 255) 
        b = int((matriz_img[i, j][2]/255) ** gamma * 255) 

        matriz_img[i, j] = (r, g, b)

img.save('img/uefs_gamma.jpeg')