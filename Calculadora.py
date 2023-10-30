from tkinter import *

class Calc:

    def __init__(self):
        # Criando a janela
        self.janela = Tk()
        self.janela.title('Calculadora')
        self.janela.resizable(0, 0)

        # Entry (visor da calculadora)
        self.tela_numeros = Entry(self.janela, font='arial 25', bg='#1d2f38', fg='#fff', width=15)
        self.tela_numeros.pack()

        # Frame (que irá conter os botões)
        self.frame = Frame(self.janela)
        self.frame.pack()

        # Botões de números
        self.botao_1 = Button(self.frame, bg='#fff', bd=1, text='1', font='arial 15 bold', fg='#333', width=5, height=2, command=lambda: self.click('1'))

        self.botao_2 = Button(self.frame, bg='#fff', bd=1, text='2', font='arial 15 bold', fg='#333', width=5, height=2, command=lambda: self.click('2'))

        self.botao_3 = Button(self.frame, bg='#fff', bd=1, text='3', font='arial 15 bold', fg='#333', width=5, height=2, command=lambda: self.click('3'))

        self.botao_4 = Button(self.frame, bg='#fff', bd=1, text='4', font='arial 15 bold', fg='#333', width=5, height=2, command=lambda: self.click('4'))

        self.botao_5 = Button(self.frame, bg='#fff', bd=1, text='5', font='arial 15 bold', fg='#333', width=5, height=2, command=lambda: self.click('5'))

        self.botao_6 = Button(self.frame, bg='#fff', bd=1, text='6', font='arial 15 bold', fg='#333', width=5, height=2, command=lambda: self.click('6'))

        self.botao_7 = Button(self.frame, bg='#fff', bd=1, text='7', font='arial 15 bold', fg='#333', width=5, height=2, command=lambda: self.click('7'))

        self.botao_8 = Button(self.frame, bg='#fff', bd=1, text='8', font='arial 15 bold', fg='#333', width=5, height=2, command=lambda: self.click('8'))

        self.botao_9 = Button(self.frame, bg='#fff', bd=1, text='9', font='arial 15 bold', fg='#333', width=5, height=2, command=lambda: self.click('9'))

        self.botao_0 = Button(self.frame, bg='#fff', bd=1, text='0', font='arial 15 bold', fg='#333', width=5, height=2, command=lambda: self.click('0'))

        # Botões dos operadores e funções
        self.botao_adicionar = Button(self.frame, bg='#fff', bd=1, text='+', font='arial 15 bold', fg='#333', width=5, height=2, command=lambda: self.click('+'))

        self.botao_sub = Button(self.frame, bg='#fff', bd=1, text='-', font='arial 15 bold', fg='#333', width=5, height=2, command=lambda: self.click('-'))

        self.botao_mult = Button(self.frame, bg='#fff', bd=1, text='*', font='arial 15 bold', fg='#333', width=5, height=2, command=lambda: self.click('*'))

        self.botao_dividir = Button(self.frame, bg='#fff', bd=1, text='/', font='arial 15 bold', fg='#333', width=5, height=2, command=lambda: self.click('/'))

        self.botao_igual = Button(self.frame, bg='#fff', bd=1, text='=', font='arial 15 bold', fg='#333', width=5, height=2, command=self.total)

        self.botao_limpar = Button(self.frame, bg='#fff', bd=1, text='C', font='arial 15 bold', fg='#333', width=5, height=2, command=self.limpar)

        # Posição dos botões
        self.botao_1.grid(row=0, column=0)
        self.botao_2.grid(row=0, column=1)
        self.botao_3.grid(row=0, column=2)
        self.botao_adicionar.grid(row=0, column=3)
        self.botao_4.grid(row=1, column=0)
        self.botao_5.grid(row=1, column=1)
        self.botao_6.grid(row=1, column=2)
        self.botao_sub.grid(row=1, column=3)
        self.botao_7.grid(row=2, column=0)
        self.botao_8.grid(row=2, column=1)
        self.botao_9.grid(row=2, column=2)
        self.botao_mult.grid(row=2, column=3)      
        self.botao_dividir.grid(row=3, column=3)
        self.botao_limpar.grid(row=3, column=1)
        self.botao_igual.grid(row=3, column=2)
        self.botao_0.grid(row=3, column=0)

        self.janela.mainloop()

    # Função para inserir dados no visor da calculadora
    def click(self, num):
        self.tela_numeros.insert(END, num)

    # Função para limpar dados no visor da calculadora
    def limpar(self):
        self.tela_numeros.delete(0, END)

    def total(self):
        t = eval(self.tela_numeros.get())
        self.tela_numeros.delete(0, END)
        self.tela_numeros.insert(0, str(t))

# Chamando a classe Calc
Calc()
