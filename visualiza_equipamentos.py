# -*- coding: utf-8 -*-
from tkinter import *
from bd import Banco


def visualiza_equipamentos():
    bd = Banco('tb_equipamentos.bd')

    def preenche_lista_equipamentos():
        lista_equipamentos.delete(0, END)
        for colunas_visu_equipamento in bd.visu_equipamento():
            lista_equipamentos.insert(END, colunas_visu_equipamento)

    janela_visualiza_equipamentos = Toplevel()

    janela_visualiza_equipamentos.title("Visualização de equipamentos")

    janela_visualiza_equipamentos.geometry("750x400")
    janela_visualiza_equipamentos.configure(bg='#2c3531')

    lista_equipamentos = Listbox(janela_visualiza_equipamentos, height=16, width=90, border=0,
                                 font=('Trebuchet MS', 12), bg='#116466', fg='#d1e8e2')
    lista_equipamentos.grid(row=0, column=0, columnspan=12, rowspan=12, padx=15, pady=15, sticky='NW')

    preenche_lista_equipamentos()
