# -*- coding: utf-8 -*-
from tkinter import *
from bd import Banco


def visualiza_chamados():
    bd = Banco('tb_chamados.bd')

    def preenche_lista_chamados():
        lista_chamados.delete(0, END)
        for colunas_visu_chamados in bd.visu_chamado():
            lista_chamados.insert(END, colunas_visu_chamados + ('dias em aberto',))

    janela_visualiza_chamados = Toplevel()

    janela_visualiza_chamados.title("Visualização de chamados")

    janela_visualiza_chamados.geometry("750x400")
    janela_visualiza_chamados.configure(bg='#2c3531')

    lista_chamados = Listbox(janela_visualiza_chamados, height=16, width=90, border=0,
                                 font=('Trebuchet MS', 12), bg='#116466', fg='#d1e8e2')
    lista_chamados.grid(row=0, column=0, columnspan=12, rowspan=12, padx=15, pady=15, sticky='NW')

    preenche_lista_chamados()
