from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

# Conexão com o banco
def get_db():
    return psycopg2.connect(
        dbname="gym",
        user="diasbrasilio",
        password="172912@Amor",
        host="localhost",
        port="5432"
    )

# Rota para listar alunos
@app.route("/alunos", methods=["GET"])
def listar_alunos():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, nome, email FROM usuarios WHERE tipo='aluno'")
    alunos = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{"id": a[0], "nome": a[1], "email": a[2]} for a in alunos])

# Rota para criar aluno
@app.route("/alunos", methods=["POST"])
def criar_aluno():
    dados = request.json
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO usuarios (nome, email, tipo, senha) VALUES (%s, %s, 'aluno', %s)",
        (dados["nome"], dados["email"], dados["senha"])
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"status": "Aluno criado com sucesso"})

# Rota para listar instrutores
@app.route("/instrutores", methods=["GET"])
def listar_instrutores():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, nome, email FROM usuarios WHERE tipo='instrutor'")
    instrutores = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{"id": i[0], "nome": i[1], "email": i[2]} for i in instrutores])

# Rota para criar instrutor
@app.route("/instrutores", methods=["POST"])
def criar_instrutor():
    dados = request.json
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO usuarios (nome, email, tipo, senha) VALUES (%s, %s, 'instrutor', %s)",
        (dados["nome"], dados["email"], dados["senha"])
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"status": "Instrutor criado com sucesso"})

# Rota de login
@app.route("/login", methods=["POST"])
def login():
    dados = request.json
    email = dados.get("email")
    senha = dados.get("senha")
    tipo = dados.get("tipo")

    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, nome, tipo FROM usuarios WHERE email=%s AND senha=%s AND tipo=%s",
        (email, senha, tipo)
    )
    usuario = cur.fetchone()
    cur.close()
    conn.close()

    if usuario:
        return jsonify({
            "status": "ok",
            "id": usuario[0],
            "nome": usuario[1],
            "tipo": usuario[2]
        })
    else:
        return jsonify({"status": "erro", "mensagem": "Credenciais inválidas"})

# Iniciar servidor
if __name__ == "__main__":
    app.run(debug=True)