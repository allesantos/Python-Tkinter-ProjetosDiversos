from tkinter import *

def NovoArquivo():
    text_area.delete(1.0, 'end')

def Salvar():
    container = text_area.get(1.0, 'end')
    arquivo = open('notepad.txt', 'w')
    arquivo.write(container)
    arquivo.close()

def Abrir():
    arquivo = open('notepad.txt', 'r')
    container = arquivo.read()
    text_area.insert(1.0, container)

def AtualizarFonte():
    fonte = spin_tipo_fonte.get()
    tamanho = spin_tamanho_fonte.get()
    text_area.config(font='{} {}'.format(fonte, tamanho))

# Criando a janela
janela = Tk()
janela.title('Bloco de Notas')
janela.geometry('830x520')
janela.minsize(width=640, height=480)

# Frame
frame = Frame(janela)
frame.pack(fill='x')

# Tipo de Fonte
tipo_fonte = Label(frame, text='Fonte: ')
tipo_fonte.pack(side='left')

spin_tipo_fonte = Spinbox(frame, values=('Arial', 'Verdana', 'Courier', 'Centaur'))
spin_tipo_fonte.pack(side='left')

# Tamanho da Fonte
tamanho_fonte = Label(frame, text='Tamanho da Fonte: ', width=20)
tamanho_fonte.pack(side='left')

spin_tamanho_fonte = Spinbox(frame, from_=0, to=60)
spin_tamanho_fonte.pack(side='left')

# Botão
button_atualizar = Button(frame, text='UP', command=AtualizarFonte)
button_atualizar.pack(side='left')


# Area de texto
text_area = Text(janela, font='Arial 12', width=1280, height=720)
text_area.pack()

# Area de menu
menu_principal = Menu(janela)

# Area de menu - Menu Arquivo
menu_arquivo = Menu(menu_principal, tearoff=0)
menu_arquivo.add_command(label='Novo', command=NovoArquivo)
menu_arquivo.add_command(label='Salvar', command=Salvar)
menu_arquivo.add_command(label='Abrir', command=Abrir)
menu_arquivo.add_command(label='Sair', command=janela.quit)
menu_principal.add_cascade(label='Arquivo', menu=menu_arquivo)

janela.config(menu=menu_principal) 

janela.mainloop()