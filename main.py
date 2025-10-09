from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def ola_mundo():
    return 'oi'

@app.route('/login')
def login_sistema():
    return render_template('login.html')


@app.route('/usuario/cadastros')
def inserir_usuario():
     return render_template('usuario/cadastro.html')

@app.route('/usuario/lista')
def lista_usuario():
    return render_template('usuario/listar.html')

if __name__ == '__main__':
    app.run(debug=True)
   