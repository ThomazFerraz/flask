from flask import Flask, render_template

app = Flask(__name__)

# CRIAR FRONTPAGE:
# Toda pagina tem um route e uma função.
# route -> enderecodosite.com/route  (ex: thotoreto.com/usuarios)
# funcao -> conteudo a ser exibido na página
# template -> edicao html


@app.route('/')  # Decorator: Sua funcao é atribuir uma funcionalidade para a função abaixo.
def homepage():
    return render_template('homepage.html')


@app.route('/contatos')
def contatos():
    return render_template('contatos.html')


@app.route('/user/<username>')
def user(username):
    return render_template('user.html', username=username)

# COLOCAR SITE NO AR: (Pesquisar hosts)


if __name__ == "__main__":
    app.run(debug=True)

