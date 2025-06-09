from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def ola():
    listaJogos = ['Tetris', 'Skyrim', 'Crash']
    return render_template('list.html', title='Jogos', jogos=listaJogos)

app.run(host='0.0.0.0')