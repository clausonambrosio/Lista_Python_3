from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para armazenar os filmes
filmes = []

class Filme:
    def __init__(self, titulo, genero, ano):
        self.titulo = titulo
        self.genero = genero
        self.ano = ano
        self.disponivel = True

@app.route('/')
def index():
    return redirect(url_for('filmes'))

@app.route('/adicionar_filme', methods=['GET', 'POST'])
def adicionar_filme():
    if request.method == 'POST':
        titulo = request.form['titulo']
        genero = request.form['genero']
        ano = request.form['ano']
        filme = Filme(titulo, genero, ano)
        filmes.append(filme)
        return redirect(url_for('filmes'))
    return render_template('adicionar_filme.html')

@app.route('/filmes')
def filmes():
    return render_template('filmes.html', filmes=filmes)

@app.route('/alugar/<int:filme_id>')
def alugar_filme(filme_id):
    filmes[filme_id].disponivel = False
    return redirect(url_for('filmes'))

@app.route('/devolver/<int:filme_id>')
def devolver_filme(filme_id):
    filmes[filme_id].disponivel = True
    return redirect(url_for('filmes'))

if __name__ == '__main__':
    app.run(debug=True)