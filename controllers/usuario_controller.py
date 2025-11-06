from main import app
from flask import request, render_template, redirect, url_for
from models.usuario_model import *
# Criando a sessão para interagir com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# rotas
@app.route("/")
def inserir_usuario():
   return render_template("usuario/cadastro.html")


@app.route("/usuario/create", methods=['POST'])
def create_usuario():
 if request.method == 'POST':
 # Captura os dados enviados pelo formulário
    nome = request.form['nome']
    login = request.form['login']
    senha = request.form['senha']
    email = request.form['email']
    telefone = request.form['telefone']
    # Cria um novo usuário
    new_user = Usuario(nome=nome,login=login,senha=senha, email=email,
    telefone=telefone)
   # Cria um novo usuário no banco de dados
 db = SessionLocal()
 # Adiciona o novo usuário ao banco de dados
 db.add(new_user)
 db.commit()
 return redirect(url_for('lista_usuario'))

@app.route("/usuario/listar")
def lista_usuario():
   db = SessionLocal()
   # Consultar todos os usuários
   usuarios = db.query(Usuario).all()
   # Renderizar o HTML passando os dados
   return render_template('usuario/listar.html', usuarios_teste=usuarios)