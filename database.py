import sqlite3

def criar_banco_dados():
    conn = sqlite3.connect('controle_financeiro.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS despesas (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 descricao TEXT NOT NULL,
                 valor REAL NOT NULL,
                 data TEXT NOT NULL)''')

    c.execute('''CREATE TABLE IF NOT EXISTS receitas (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 descricao TEXT NOT NULL,
                 valor REAL NOT NULL,
                 data TEXT NOT NULL)''')

    conn.commit()
    conn.close()

criar_banco_dados()
