from tkinter import *
from tkinter.ttk import *
from time import strftime

janela = Tk()
janela.title('Relógio Digital')

def time():
    relogio = strftime('%H:%M:%S %p')
    lbl.config(text = relogio)
    lbl.after(1000, time)

lbl = Label(janela, font = ('arial', 40, 'bold'),
         background ='black', foreground='white')
lbl.pack(anchor = 'center')

time()

mainloop()


