from tkinter import *

# Função do botão Calcular
def calcular():
    n1 = int(ent1.get())
    n2 = int(ent2.get())
    res = n1 + n2
    lbl_res = Label(janela, text=f'{res}', anchor='w', font='Arial 16 bold', fg='#ff0000').place(x=110, y=228)

# Janela
janela = Tk()

janela.geometry('300x280')
janela.title('')
janela.resizable(False, False)

# Título Principal
lbl0 = Label(janela, text='Calculadora Soma Fácil!', font='Arial 16 bold italic', fg='#ff0000')
lbl0.place(x=20, y=30)

# Label do Valor 1
lbl1 = Label(janela, text='Valor 1:', font='Arial 12 bold', fg='#0000ff', anchor='s')
lbl1.place(height=30, x= 20, y=80)

# Label do Valor 2
lbl2 = Label(janela, text='Valor 2:', font='Arial 12 bold', fg='#0000ff', anchor='s')
lbl2.place(height=30, x= 20, y=120)

# Label do Resultado
lbl3 = Label(janela, text='Resultado:', anchor='w', font='Arial 12 bold', fg='#0000ff')
lbl3.place(x= 20, y=232)

# Caixa de Entrada do Valor 1
ent1 = Entry(janela, font='Arial 12 bold')
ent1.place(width=60, height=30, x=90, y=80)

# Caixa de Entrada do Valor 2
ent2 = Entry(janela, font='Arial 12 bold')
ent2.place(width=60, height=30, x=90, y=120)

# Botão Calcular
btn = Button(janela, text='Calcular', font='Arial 12',command=calcular)
btn.place(width=80, x=50, y=175)

janela.mainloop()