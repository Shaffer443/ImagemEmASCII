from image_to_ascii import ImageToAscii

obj = ImageToAscii()

# Endereço da Imagem:

obj.image_path("IMG_20180807_122432077_1.jpg")

# Imprimir na Tela:

obj.plot()

# salvar  e Exportar (criando) um arquivo .txt:

obj.save_to_file()
