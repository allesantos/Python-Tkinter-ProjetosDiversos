# Importações ===========================

from tkinter import *
from tkinter import ttk
from tkinter import messagebox  
from PIL import ImageTk, Image 
import random
import string

# Cores =================================

cor0 = "#2d2c2c"  # Preto
cor1 = "#feffff"  # Branco
cor2 = "#6f9fbd"  # Azul
cor3 = "#dc1a1f"  # Vermelho

fundo_dark="#484f60"
fundo_claro = "#fff"

fundo = cor1

# Criação da janela =====================

janela = Tk()
janela.title('')
janela.geometry('300x360')
janela.configure(bg=fundo)

estilo = ttk.Style(janela)
estilo.theme_use("clam")

# Frames ================================

frame_superior = Frame(janela, width=300, height=110,bg=fundo, pady=0, padx=0, relief="flat",)
frame_superior.grid(row=0, column=0)

frame_inferior = Frame(janela, width=300, height=220,bg=fundo, pady=0, padx=0, relief="flat",)
frame_inferior.grid(row=1, column=0)

# Frame superior ========================

img_0 = Image.open('senha.png')
img_0 = img_0.resize((30, 30), Image.LANCZOS)
img_0 = ImageTk.PhotoImage(img_0)

app_imagem = Label(frame_superior,  height=60, image=img_0, compound=LEFT,padx=10, relief="flat", anchor="nw", font=('Ivy 16 bold'), bg=cor1, fg=cor3)
app_imagem.place(x=2, y=0)
app_name = Label(frame_superior, text="GERADOR DE SENHAS", width=20, height=1, padx=0, relief="flat", anchor="nw", font=('Ivy 16 bold'), bg=cor1, fg=cor0)
app_name.place(x=35, y=2)

app_linha = Label(frame_superior, text="", width=400, height=1, padx=0, relief="flat", anchor="nw", font=('Arial 1'), bg=cor3, fg=cor1)
app_linha.place(x=0, y=36)

# Função para gerar a senha ============

def criar_senha():
    alfabeto_menos = string.ascii_lowercase
    alfabeto_mais = string.ascii_uppercase
    numeros = '123456789'
    simbolos = "[]{}()*;/,_-"
    
    global combinar
    
    # --- Condição para maiusculas
    if estado_1.get() == alfabeto_mais:
        combinar = alfabeto_mais
    else:
        pass
    
    # --- Condição para minuscula
    if estado_2.get() == alfabeto_menos:
        combinar = combinar + alfabeto_menos
    else:
        pass
    
    # --- Condição para números
    if estado_3.get() == numeros:
        combinar = combinar + numeros
    else:
        pass
    
    # --- Condição para símbolos
    if estado_4.get() == simbolos:
        combinar = combinar + simbolos
    else:
        pass
    
    # --- Comprimento da senha
    comprimento = int(spin.get())
    
    # --- Senha
    senha = "".join(random.sample(combinar, comprimento))
    app_senha['text'] = senha
    
    # Função para copiar a senha =======================
    
    def copiar_senha():
        info = senha
        frame_inferior.clipboard_clear()
        frame_inferior.clipboard_append(info)
        messagebox.showinfo("Sucesso","A senha foi copiada com sucesso") 
        
    b_copiar = Button(frame_inferior, command=copiar_senha, text="Copiar",width=7, height=1, overrelief=SOLID,  bg=cor1, fg=cor0, font=('Ivy 10 bold'), anchor="center", relief=RAISED )
    b_copiar.grid(row=0, column=2, columnspan=2,  sticky=NSEW, pady=10, padx=1)
    

alfabeto_menos = string.ascii_lowercase
alfabeto_mais = string.ascii_uppercase
numeros = '123456789'
simbolos = "[]{}()*;/,_-"

var =IntVar()
var.set(8)
app_info = Label(frame_superior, text="Número total de caracteres na senha", height=1, padx=0, relief="flat", anchor="nw", font=('Ivy 10 bold'), bg=fundo, fg=cor0)
app_info.place(x=15, y=60)
spin = Spinbox(frame_superior, from_=0, to=20, width=5, textvariable=var)
spin.place(x=20, y=90)

app_senha = Label(frame_inferior , text="- - -", width=20, height=2, padx=0, relief="solid", anchor="center", font=('Ivy 10 bold'), bg=fundo, fg=cor0)
app_senha.grid(row=0, column=0, columnspan=2,  sticky=NSEW, pady=10, padx=2)

# Letras maiúsculas =======================

app_info = Label(frame_inferior, text="ABC Letras maiúsculas", height=1, padx=0, relief="flat", anchor="nw",justify='center', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
app_info.grid(row=1, column=1,  sticky=NSEW, pady=5, padx=2)
    
estado_1 = StringVar()
estado_1.set(False) 
chek_1 = Checkbutton(frame_inferior,width=1, var=estado_1,onvalue=alfabeto_mais, offvalue='off', bg=fundo)
chek_1.grid(row=1, column=0,  sticky=NSEW, pady=5, padx=2)

# Letras minúsculas ========================

app_info = Label(frame_inferior, text="abc Letras minúsculas", height=1, padx=0, relief="flat", anchor="nw",justify='center', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
app_info.grid(row=2, column=1,  sticky=NSEW, pady=5, padx=2)
    
estado_2 = StringVar()
estado_2.set(False)  
chek_2 = Checkbutton(frame_inferior,width=1, var=estado_2,onvalue=alfabeto_menos, offvalue='off',bg=fundo)
chek_2.grid(row=2, column=0,  sticky=NSEW, pady=5, padx=2)

# Números ==================================

app_info = Label(frame_inferior, text="123 Números",height=1, padx=0, relief="flat", anchor="nw",justify='center', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
app_info.grid(row=3, column=1,  sticky=NSEW, pady=5, padx=2)

estado_3 = StringVar()
estado_3.set(False)  # set check state
chek_3 = Checkbutton(frame_inferior,width=1, var=estado_3,onvalue=numeros, offvalue='off',bg=fundo)
chek_3.grid(row=3, column=0,  sticky=NSEW, pady=5, padx=2)

# Símbolos ================================

app_info = Label(frame_inferior, text="!@# Símbolos", height=1, padx=0, relief="flat", anchor="nw",justify='center', font=('Ivy 10 bold'), bg=cor1, fg=cor0)
app_info.grid(row=4, column=1,  sticky=NSEW, pady=1, padx=2)

estado_4 = StringVar()
estado_4.set(False)  
chek_4 = Checkbutton(frame_inferior,width=1, var=estado_4, onvalue=simbolos, offvalue='off',bg=fundo)
chek_4.grid(row=4, column=0,  sticky=NSEW, pady=1, padx=2)

# Botão Gerar senha =======================

b_gerar_senha = Button(frame_inferior, command=criar_senha, text="Gerar senha",width=32, height=1, overrelief=SOLID,  bg=cor3, fg="white", font=('Ivy 10 bold'), anchor="center", relief=FLAT )
b_gerar_senha.grid(row=5, column=0,  sticky=NSEW, pady=20, padx=0, columnspan=5)

janela.mainloop()