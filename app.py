from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # Defina uma chave secreta para usar sessões

# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect('db.sqlite3')
    conn.row_factory = sqlite3.Row  # Permite acessar os dados por nome de coluna
    return conn

# Função para inicializar o banco de dados e criar a tabela contatos
def init_db():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT,
        motivo TEXT NOT NULL
    )''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contato', methods=['POST'])
def contato():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    motivo = request.form['motivo']

    try:
        # Conectando ao banco de dados e inserindo os dados
        conn = get_db_connection()
        conn.execute(
            'INSERT INTO contatos (nome, email, telefone, motivo) VALUES (?, ?, ?, ?)',
            (nome, email, telefone, motivo)
        )
        conn.commit()
        conn.close()

        flash('Dados enviados com sucesso!', 'success')  # Mensagem de sucesso
    except Exception as e:
        flash(f'Erro ao inserir dados: {e}', 'error')  # Mensagem de erro

    return redirect(url_for('index'))

@app.route('/contatos')
def listar_contatos():
    conn = get_db_connection()
    contatos = conn.execute('SELECT * FROM contatos').fetchall()
    conn.close()
    return render_template('contatos.html', contatos=contatos)

if __name__ == '__main__':
    init_db()  # Inicializa o banco de dados
    app.run(debug=True)
