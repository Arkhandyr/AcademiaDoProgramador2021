# -*- coding: utf-8 -*-
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from bd import Banco
from visualiza_equipamentos import visualiza_equipamentos
from visualiza_chamados import visualiza_chamados
from chamados import nova_janela

bd = Banco('tb_equipamentos.bd')


def preenche_lista_equipamentos():
    lista_equipamentos.delete(0, END)
    for colunas_equipamento in bd.busca_equipamento():
        lista_equipamentos.insert(END, colunas_equipamento)


def adiciona_equipamento():
    if nome_text.get() == '' or \
            preco_text.get() == '' or \
            numero_serie_text.get() == '' or \
            data_fabricacao_text.get() == '' or \
            fabricante_text.get() == '':
        messagebox.showerror('Erro', 'Preencha todos os campos.')
        return
    elif len(nome_text.get()) <= 6:
        messagebox.showerror('Erro', 'Nome do equipamento deve ser superior a seis dígitos.')
        return
    bd.insere_equipamento(nome_text.get(), preco_text.get(), numero_serie_text.get(),
                          data_fabricacao_text.get(), fabricante_text.get())
    lista_equipamentos.delete(0, END)
    lista_equipamentos.insert(END, (nome_text.get(), preco_text.get(),
                                    numero_serie_text.get(), data_fabricacao_text.get(),
                                    fabricante_text.get()))
    limpa_texto()
    preenche_lista_equipamentos()


def seleciona_equipamento(event):
    try:
        global equipamento_selecionado
        index = lista_equipamentos.curselection()[0]
        equipamento_selecionado = lista_equipamentos.get(index)

        nome_entry.delete(0, END)
        nome_entry.insert(END, equipamento_selecionado[1])
        preco_entry.delete(0, END)
        preco_entry.insert(END, equipamento_selecionado[2])
        numero_serie_entry.delete(0, END)
        numero_serie_entry.insert(END, equipamento_selecionado[3])
        data_fabricacao_entry.delete(0, END)
        data_fabricacao_entry.insert(END, equipamento_selecionado[4])
        fabricante_entry.delete(0, END)
        fabricante_entry.insert(END, equipamento_selecionado[5])
    except IndexError:
        pass


def remove_equipamento():
    bd.remove_equipamento(equipamento_selecionado[0])
    limpa_texto()
    preenche_lista_equipamentos()


def atualiza_equipamento():
    if nome_text.get() == '' or \
            preco_text.get() == '' or \
            numero_serie_text.get() == '' or \
            data_fabricacao_text.get() == '' or \
            fabricante_text.get() == '':
        messagebox.showerror('Erro', 'Preencha todos os campos.')
        return
    elif len(nome_text.get()) < 6:
        messagebox.showerror('Erro', 'Nome do equipamento deve ser superior a seis dígitos.')
        return
    bd.atualiza_equipamento(nome_text.get(), preco_text.get(),
                            numero_serie_text.get(), data_fabricacao_text.get(),
                            fabricante_text.get(), equipamento_selecionado[0])
    preenche_lista_equipamentos()


def limpa_texto():
    nome_entry.delete(0, END)
    preco_entry.delete(0, END)
    numero_serie_entry.delete(0, END)
    data_fabricacao_entry.delete(0, END)
    fabricante_entry.delete(0, END)


app = Tk()

nome_text = StringVar()
nome_label = Label(app, text='Equipamento', font=('Trebuchet MS', 12, 'bold'), padx=10, pady=10, bg='#2c3531',
                   fg='#d1e8e2')
nome_label.grid(row=0, column=0, sticky=W)
nome_entry = Entry(app, textvariable=nome_text, font=('Trebuchet MS', 8, 'bold'), border=0, bg='#d1e8e2')
nome_entry.grid(row=0, column=1)

preco_text = StringVar()
preco_label = Label(app, text='Preço', font=('Trebuchet MS', 12, 'bold'), padx=10, bg='#2c3531', fg='#d1e8e2')
preco_label.grid(row=1, column=0, sticky=W)
preco_entry = Entry(app, textvariable=preco_text, font=('Trebuchet MS', 8, 'bold'), border=0, bg='#d1e8e2')
preco_entry.grid(row=1, column=1)

numero_serie_text = StringVar()
numero_serie_label = Label(app, text='Numero de série', font=('Trebuchet MS', 12, 'bold'), padx=10, pady=10,
                           bg='#2c3531', fg='#d1e8e2')
numero_serie_label.grid(row=2, column=0, sticky=W)
numero_serie_entry = Entry(app, textvariable=numero_serie_text, font=('Trebuchet MS', 8, 'bold'), border=0,
                           bg='#d1e8e2')
numero_serie_entry.grid(row=2, column=1)

data_fabricacao_text = StringVar()
data_fabricacao_label = Label(app, text='Data de fabricação', font=('Trebuchet MS', 12, 'bold'), padx=10, bg='#2c3531',
                              fg='#d1e8e2')
data_fabricacao_label.grid(row=3, column=0, sticky=W)
data_fabricacao_entry = Entry(app, textvariable=data_fabricacao_text, font=('Trebuchet MS', 8, 'bold'), border=0,
                              bg='#d1e8e2')
data_fabricacao_entry.grid(row=3, column=1)

fabricante_text = StringVar()
fabricante_label = Label(app, text='Fabricante', font=('Trebuchet MS', 12, 'bold'), padx=10, pady=10, bg='#2c3531',
                         fg='#d1e8e2')
fabricante_label.grid(row=4, column=0, sticky=W)
fabricante_entry = Entry(app, textvariable=fabricante_text, font=('Trebuchet MS', 8, 'bold'), border=0, bg='#d1e8e2')
fabricante_entry.grid(row=4, column=1)

lista_equipamentos = Listbox(app, height=7, width=45, border=0, font=('Trebuchet MS', 12), bg='#116466', fg='#d1e8e2')
lista_equipamentos.grid(row=5, column=0, columnspan=4, rowspan=3, padx=100, pady=10, sticky='SW')

scrollbar = Scrollbar(app)
scrollbar.grid(row=5, column=3, rowspan=3, pady=10, padx=10, sticky='NWS')
lista_equipamentos.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=lista_equipamentos.yview)

lista_equipamentos.bind('<<ListboxSelect>>', seleciona_equipamento)

add_btn = Button(app, text='Adicionar Equipamento', width=18, font=('Trebuchet MS', 9),
                 bg='#d9b08c', border=0, command=adiciona_equipamento)
add_btn.grid(row=0, column=2, pady=5, sticky='E', padx=5)

remove_btn = Button(app, text='Remover Equipamento', width=18, font=('Trebuchet MS', 9),
                    bg='#d9b08c', border=0, command=remove_equipamento)
remove_btn.grid(row=0, column=3, pady=5, sticky='W', padx=5)

update_btn = Button(app, text='Atualizar Equipamento', width=18, font=('Trebuchet MS', 9),
                    bg='#d9b08c', border=0, command=atualiza_equipamento)
update_btn.grid(row=1, column=2, pady=5, sticky='E', padx=5)

clear_btn = Button(app, text='Limpar texto', width=18, font=('Trebuchet MS', 9),
                   bg='#d9b08c', border=0, command=limpa_texto)
clear_btn.grid(row=1, column=3, pady=5, sticky='W', padx=5)


janela_visualiza_equipamento_btn = Button(app, text="Visualizar Equipamentos", width=18, bg='#d9b08c', border=0,
                                          font=('Trebuchet MS', 9), command=visualiza_equipamentos)
janela_visualiza_equipamento_btn.grid(row=2, column=2, sticky='E', pady=5, padx=5)

janela_visualiza_chamado_btn = Button(app, text="Visualizar Chamados", width=18, bg='#d9b08c', border=0,
                                          font=('Trebuchet MS', 9), command=visualiza_chamados)
janela_visualiza_chamado_btn.grid(row=2, column=3, sticky='W', padx=5, pady=5)

janela_chamados_btn = Button(app, text="Chamados", width=25, bg='#d9b08c', border=0,
                                    font=('Trebuchet MS', 14), command=nova_janela)
janela_chamados_btn.grid(row=3, column=2, padx=30, pady=10, columnspan=2, rowspan=2, sticky='NEW')

app.title('Gerenciamento de Equipamentos')
app.iconphoto(True, tk.PhotoImage(file='gerenciamento.png'))
app.geometry('600x400')
app.configure(bg='#2c3531')

preenche_lista_equipamentos()

app.mainloop()
