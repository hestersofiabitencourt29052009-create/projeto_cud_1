# banco de dados -  modelagem  

import sqlite3

def salvar_no_banco(texto):
    conn = sqlite3.connect('dados.db')
    c =  conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS notas (texto TEXT)")
    c.execute("INSERT INTO notas VALUES(?)",(texto,))
    conn.commit()
    conn.close()

def ler_do_banco():
    conn = sqlite3.connect('dados.db')
    c =  conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS notas(texto TEXT)')
    c.execute("SELECT * FROM notas")
   
    dados  =  c.fetchall()
    conn.close()
    return dados

