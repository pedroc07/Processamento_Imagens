from PIL import Image

img_eua = Image.open("sample_data/eua.tif")
img_sulamerica = Image.open("sample_data/sudamerica.tif")
img_asia = Image.open("sample_data/asia.tif")
img_australia = Image.open("sample_data/australia_nzelandia.tif")
img_americacentral = Image.open("sample_data/centroamerica.tif")
img_sudesteasia = Image.open("sample_data/sudeste_asia.tif")
img_europa_africa = Image.open("sample_data/europa_africa.tif")
img_canada = Image.open("sample_data/canada.tif")

def get_eletric(img):
    pix_brancos = 0
    total = 0
    for i in range(img.width):
        for j in range(img.height):
            pixel = img.getpixel((i, j))
            if pixel == 255:
                pix_brancos += 1
    return pix_brancos 

eletric_eua = get_eletric(img_eua)
eletric_sulamerica = get_eletric(img_sulamerica)
eletric_euro_afri = get_eletric(img_europa_africa)
eletric_asia = get_eletric(img_asia)
eletric_aust = get_eletric(img_australia)
eletric_americacentral = get_eletric(img_americacentral)
eletric_sudesteasia = get_eletric(img_sudesteasia)
eletric_canada = get_eletric(img_canada)

eletric_total_sempesos = eletric_eua + eletric_sulamerica + eletric_euro_afri + eletric_asia + eletric_aust + eletric_americacentral + eletric_sudesteasia + eletric_canada


eletric_total = eletric_eua*0.098 + eletric_sulamerica*0.178 + eletric_euro_afri*0.409 + eletric_asia*0.169 + eletric_aust*0.079 + eletric_americacentral*0.005 + eletric_sudesteasia*0.045 + eletric_canada*0.099

print(f"Percentual de Energia Elétrica dos Estados Unidos: {((eletric_eua*0.098)/eletric_total)*100}" + 
      f"\nPercentual de Energia Elétrica da América do Sul: {((eletric_sulamerica*0.178)/eletric_total)*100}" +
      f"\nPercentual de Energia Elétrica da África e Europa: {((eletric_euro_afri*0.409)/eletric_total)*100}"
      f"\nPercentual de Energia Elétrica da Ásia: {((eletric_asia*0.169)/eletric_total)*100}" +
      f"\nPercentual de Energia Elétrica da Austrália e Nova Zelândia: {((eletric_aust*0.079)/eletric_total)*100}"+
      f"\nPercentual de Energia Elétrica da América Central: {((eletric_americacentral*0.005)/eletric_total)*100}"+
      f"\nPercentual de Energia Elétrica do Sudeste Asiático: {((eletric_sudesteasia*0.045)/eletric_total)*100}"+
      f"\nPercentual de Energia Elétrica do Canadá: {((eletric_canada*0.099)/eletric_total)*100}\nTotal: 100")