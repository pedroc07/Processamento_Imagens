from PIL import Image

img_eua = Image.open("img/eua.tif")
img_sulamerica = Image.open("img/sudamerica.tif")
img_europa_africa = Image.open("img/europa_africa.tif")


def get_eletric(img):
    pix_brancos = 0
    for i in range(img.width):
        for j in range(img.height):
            pixel = img.getpixel((i, j))
            if pixel == 255:
                pix_brancos += 1
            #else:
            #    pix_pretos += 1
    return pix_brancos

eletric_eua = get_eletric(img_eua)
eletric_sulamerica = get_eletric(img_europa_africa)
eletric_euro_afri = get_eletric(img_sulamerica)

eletric_total = eletric_eua + eletric_sulamerica + eletric_euro_afri

print(f"Percentual de Energia Elétrica dos Estados Unidos: {(eletric_eua/eletric_total)*100}\nPercentual de Energia Elétrica da América do Sul: {(eletric_sulamerica/eletric_total)*100}\nPercentual de Energia Elétrica da África e Europa: {(eletric_euro_afri/eletric_total)*100}\nTotal: 100")