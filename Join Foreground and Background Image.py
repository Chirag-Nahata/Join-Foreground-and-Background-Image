from PIL import Image
me = Image.open('Chirag_Nahata.png')
bg = Image.open('Chirag_Nahata_Coder.jpg')
bg.paste(me, (0, 0), me)
bg.show()