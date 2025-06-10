from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

app = Flask(__name__)

@app.route('/')
def ola():
    jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
    jogo2 = Jogo('Stardew Valley', 'Simulação', 'Computador')
    jogo3 = Jogo('Remnant from the Ashes', 'Souls Like', 'Xbox')

    listaJogos = [jogo1, jogo2, jogo3]

    return render_template('list.html', title='Jogos', jogos=listaJogos)

app.run(host='0.0.0.0')