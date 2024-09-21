from flask import Flask, request, render_template, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'thisnotkey'  

DATABASE = 'controle_financeiro.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_despesa', methods=['POST'])
def add_despesa():
    descricao = request.form['descricao']
    valor = request.form['valor']
    data = request.form['data']
    
    if not descricao or not valor or not data:
        flash('Todos os campos devem ser preenchidos.', 'error')
        return redirect(url_for('index'))
    
    conn = get_db()
    c = conn.cursor()
    c.execute("INSERT INTO despesas (descricao, valor, data) VALUES (?, ?, ?)",
              (descricao, float(valor), data))
    conn.commit()
    conn.close()
    flash('Despesa adicionada com sucesso!', 'success')
    return redirect(url_for('index'))

@app.route('/add_receita', methods=['POST'])
def add_receita():
    descricao = request.form['descricao']
    valor = request.form['valor']
    data = request.form['data']
    
    if not descricao or not valor or not data:
        flash('Todos os campos devem ser preenchidos.', 'error')
        return redirect(url_for('index'))
    
    conn = get_db()
    c = conn.cursor()
    c.execute("INSERT INTO receitas (descricao, valor, data) VALUES (?, ?, ?)",
              (descricao, float(valor), data))
    conn.commit()
    conn.close()
    flash('Receita adicionada com sucesso!', 'success')
    return redirect(url_for('index'))

@app.route('/relatorio')
def relatorio():
    conn = get_db()
    c = conn.cursor()
    
    c.execute("SELECT SUM(valor) FROM despesas")
    total_despesas = c.fetchone()[0] or 0

    c.execute("SELECT SUM(valor) FROM receitas")
    total_receitas = c.fetchone()[0] or 0

    saldo = total_receitas - total_despesas

    conn.close()
    
    return render_template('relatorio.html', total_despesas=total_despesas, total_receitas=total_receitas, saldo=saldo)

if __name__ == '__main__':
    app.run(debug=True)

