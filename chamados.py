# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
from bd import Banco


def nova_janela():
    bd = Banco('tb_chamados.bd')

    def preenche_lista_chamados():
        lista_chamados.delete(0, END)
        for colunas_chamados in bd.busca_chamado():
            lista_chamados.insert(END, colunas_chamados)

    def adiciona_chamado():
        if titulo_text.get() == '' or \
                descricao_text.get() == '' or \
                equipamento_text.get() == '' or \
                data_de_abertura_text.get() == '':
            messagebox.showerror('Erro', 'Preencha todos os campos.', parent=janela_chamados)
            return
        bd.insere_chamado(titulo_text.get(), descricao_text.get(), equipamento_text.get(),
                          data_de_abertura_text.get())
        lista_chamados.delete(0, END)
        lista_chamados.insert(END, (titulo_text.get(), descricao_text.get(),
                                    equipamento_text.get(), data_de_abertura_text.get()))
        limpa_texto_chamado()
        preenche_lista_chamados()

    def seleciona_chamado(event):
        try:
            global chamado_selecionado
            index = lista_chamados.curselection()[0]
            chamado_selecionado = lista_chamados.get(index)

            titulo_entry.delete(0, END)
            titulo_entry.insert(END, chamado_selecionado[1])
            descricao_entry.delete(0, END)
            descricao_entry.insert(END, chamado_selecionado[2])
            equipamento_entry.delete(0, END)
            equipamento_entry.insert(END, chamado_selecionado[3])
            data_de_abertura_entry.delete(0, END)
            data_de_abertura_entry.insert(END, chamado_selecionado[4])
        except IndexError:
            pass

    def remove_chamado():
        bd.remove_chamado(chamado_selecionado[0])
        limpa_texto_chamado()
        preenche_lista_chamados()

    def atualiza_chamado():
        bd.atualiza_chamado(titulo_text.get(), descricao_text.get(),
                            equipamento_text.get(), data_de_abertura_text.get(),
                            chamado_selecionado[0])
        preenche_lista_chamados()

    def limpa_texto_chamado():
        titulo_entry.delete(0, END)
        descricao_entry.delete(0, END)
        equipamento_entry.delete(0, END)
        data_de_abertura_entry.delete(0, END)

    janela_chamados = Toplevel()

    janela_chamados.title("Controle de Chamados")

    janela_chamados.geometry('600x400')
    janela_chamados.configure(bg='#2c3531')

    titulo_text = StringVar()
    titulo_label = Label(janela_chamados, text='Título', font=('Trebuchet MS', 12, 'bold'),
                         padx=10, pady=10, bg='#2c3531', fg='#d1e8e2')
    titulo_label.grid(row=0, column=0, sticky=W)
    titulo_entry = Entry(janela_chamados, textvariable=titulo_text, border=0, bg='#d1e8e2')
    titulo_entry.grid(row=0, column=1)

    descricao_text = StringVar()
    descricao_label = Label(janela_chamados, text='Descrição', font=('Trebuchet MS', 12, 'bold'),
                            padx=10, pady=10, bg='#2c3531', fg='#d1e8e2')
    descricao_label.grid(row=1, column=0, sticky=W)
    descricao_entry = Entry(janela_chamados, textvariable=descricao_text, border=0, bg='#d1e8e2')
    descricao_entry.grid(row=1, column=1)

    equipamento_text = StringVar()
    equipamento_label = Label(janela_chamados, text='Equipamento', font=('Trebuchet MS', 12, 'bold'),
                              padx=10, pady=10, bg='#2c3531', fg='#d1e8e2')
    equipamento_label.grid(row=2, column=0, sticky=W)
    equipamento_entry = Entry(janela_chamados, textvariable=equipamento_text, border=0, bg='#d1e8e2')
    equipamento_entry.grid(row=2, column=1)

    data_de_abertura_text = StringVar()
    data_de_abertura_label = Label(janela_chamados, text='Data de abertura', font=('Trebuchet MS', 12, 'bold'),
                                   padx=10, pady=10, bg='#2c3531', fg='#d1e8e2')
    data_de_abertura_label.grid(row=3, column=0, sticky=W)
    data_de_abertura_entry = Entry(janela_chamados, textvariable=data_de_abertura_text, border=0, bg='#d1e8e2')
    data_de_abertura_entry.grid(row=3, column=1)

    lista_chamados = Listbox(janela_chamados, height=7, width=50, border=0, font=('Trebuchet MS', 12), bg='#116466',
                             fg='#d1e8e2')
    lista_chamados.grid(row=4, column=0, columnspan=4, rowspan=3, padx=100, pady=10, sticky='SW')

    scrollbar2 = Scrollbar(janela_chamados)
    scrollbar2.grid(row=4, column=3, rowspan=3, pady=10, padx=40, sticky='NWS')
    lista_chamados.configure(yscrollcommand=scrollbar2.set)
    scrollbar2.configure(command=lista_chamados.yview)

    scrollbar3 = Scrollbar(janela_chamados, orient='horizontal')
    scrollbar3.grid(row=6, column=0, columnspan=4, pady=10, padx=100, sticky='WSE')
    lista_chamados.configure(xscrollcommand=scrollbar3.set)
    scrollbar3.configure(command=lista_chamados.xview)

    lista_chamados.bind('<<ListboxSelect>>', seleciona_chamado)

    add_btn = Button(janela_chamados, text='Registrar Chamado', width=18, font=('Trebuchet MS', 9),
                     bg='#d9b08c', border=0, command=adiciona_chamado)
    add_btn.grid(row=1, column=2, pady=5, sticky='E', padx=5)

    remove_btn = Button(janela_chamados, text='Remover Chamado', width=18, font=('Trebuchet MS', 9),
                        bg='#d9b08c', border=0, command=remove_chamado)
    remove_btn.grid(row=1, column=3, pady=5, sticky='W', padx=5)

    update_btn = Button(janela_chamados, text='Atualizar Chamado', width=18, font=('Trebuchet MS', 9),
                        bg='#d9b08c', border=0, command=atualiza_chamado)
    update_btn.grid(row=2, column=2, pady=5, sticky='E', padx=5)

    clear_btn = Button(janela_chamados, text='Limpar texto', width=18, font=('Trebuchet MS', 9),
                       bg='#d9b08c', border=0, command=limpa_texto_chamado)
    clear_btn.grid(row=2, column=3, pady=5, sticky='W', padx=5)

    preenche_lista_chamados()
