from flask import Flask, render_template, request, redirect, session, flash

class Game:
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console

game1 = Game('Tetris', 'Puzzle', 'Atari')
game2 = Game('Stardew Valley', 'Simulação', 'Computador')
game3 = Game('Remnant from the Ashes', 'Souls Like', 'Xbox')
gameList = [game1, game2, game3]

app = Flask(__name__)
app.secret_key = 'alura'

@app.route('/')
def index():
    return render_template('list.html', title='Jogos', games=gameList)

@app.route('/new')
def newGame():
    return render_template('new.html', title='Novo Jogo')

@app.route('/create', methods=['POST',])
def createGame():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']

    game = Game(name, category, console)

    gameList.append(game)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/authenticate', methods=['POST',])
def authenticate():
    if request.form['password'] =='alohomora':
        session['user_loged'] = request.form['user']
        flash(f'Usuário {session['user_loged']} logado com sucesso!')
        return redirect('/')
    else:
        flash('Usuário não logado')
        return redirect('/login')


app.run(debug=True)