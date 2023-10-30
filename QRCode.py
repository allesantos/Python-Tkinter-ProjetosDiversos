import qrcode
from tkinter import *

def gerar():
    qr = qrcode.QRCode(
        version=1,
        box_size=10, 
        border=4, 
        )
    qr.add_data('https://www.youtube.com/@CursosAlleDigital') 
    qr.make(fit=True)

    img = qr.make_image(fill_color='black', back_color='white') 
    img.save('qr_canal.png') 

janela = Tk()
janela.geometry('200x130')
janela.title('')

Label(janela, text='Gerador de QR Code', font='Arial 12').place(x= 20, y=10)

Button(janela, text='Gerar', height=2, width=5, command=gerar).place(x= 70, y= 50)

janela.mainloop()
