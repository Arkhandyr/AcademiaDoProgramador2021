# -*- coding: utf-8 -*-
import sqlite3


class Banco:
    def __init__(self, bd):
        self.conn = sqlite3.connect(bd)
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS tb_equipamentos (
                 id_equip integer PRIMARY KEY NOT NULL,
                 nome varchar(64),
                 preco double,
                 numero_serie integer,
                 data_fabricacao text,
                 fabricante varchar(64))""")
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS tb_chamados (
                 id_chamado integer PRIMARY KEY NOT NULL,
                 titulo varchar(64),
                 descricao varchar(64),
                 equipamento varchar(64),
                 data_de_abertura real,
                 FOREIGN KEY (equipamento) REFERENCES tb_equipamentos(nome))""")
        self.conn.commit()

    def busca_equipamento(self):
        self.cur.execute("SELECT * FROM tb_equipamentos")
        colunas_equipamento = self.cur.fetchall()
        return colunas_equipamento

    def visu_equipamento(self):
        self.cur.execute("SELECT nome, numero_serie, fabricante FROM tb_equipamentos")
        colunas_visu_equipamento = self.cur.fetchall()
        return colunas_visu_equipamento

    def busca_chamado(self):
        self.cur.execute("SELECT * FROM tb_chamados")
        colunas_chamado = self.cur.fetchall()
        return colunas_chamado

    def visu_chamado(self):
        self.cur.execute("""
            SELECT titulo, equipamento, data_de_abertura, 
            julianday('now', 'start of day') - julianday(data_de_abertura, 'start of day') 
            FROM tb_chamados""")
        colunas_visu_chamado = self.cur.fetchall()
        return colunas_visu_chamado

    def insere_equipamento(self, nome, preco, numero_serie, data_fabricacao, fabricante):
        self.cur.execute("INSERT INTO tb_equipamentos VALUES (NULL, ?, ?, ?, ?, ?)",
                         (nome, preco, numero_serie, data_fabricacao, fabricante))
        self.conn.commit()

    def insere_chamado(self, titulo, descricao, equipamento, data_de_abertura):
        self.cur.execute("INSERT INTO tb_chamados VALUES (NULL, ?, ?, ?, ?)",
                         (titulo, descricao, equipamento, data_de_abertura))
        self.conn.commit()

    def remove_equipamento(self, id_equip):
        self.cur.execute("DELETE FROM tb_equipamentos WHERE id_equip=?", (id_equip,))
        self.conn.commit()

    def remove_chamado(self, id_chamado):
        self.cur.execute("DELETE FROM tb_chamados WHERE id_chamado=?", (id_chamado,))
        self.conn.commit()

    def atualiza_equipamento(self, nome, preco, numero_serie, data_fabricacao, fabricante, id_equip):
        self.cur.execute("""
        UPDATE tb_equipamentos SET 
        nome = ?, 
        preco = ?,
        numero_serie = ?, 
        data_fabricacao = ?, 
        fabricante = ?
        WHERE id_equip = ?""", (nome, preco, numero_serie, data_fabricacao, fabricante, id_equip))
        self.conn.commit()

    def atualiza_chamado(self, titulo, descricao, equipamento, data_de_abertura, id_chamado):
        self.cur.execute("""
        UPDATE tb_chamados SET 
        titulo = ?, 
        descricao = ?,
        equipamento = ?, 
        data_de_abertura = ? 
        WHERE id_chamado = ?""", (titulo, descricao, equipamento, data_de_abertura, id_chamado))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
