from flask import Flask, render_template, request, redirect, session, flash, url_for

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
    if 'logged_user' not in session or session['logged_user'] == None:
        return redirect(url_for('login', next=url_for('newGame')))

    return render_template('new.html', title='Novo Jogo')

@app.route('/create', methods=['POST',])
def createGame():
    name = request.form['name']
    category = request.form['category']
    console = request.form['console']

    game = Game(name, category, console)

    gameList.append(game)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    next = request.args.get('next')
    return render_template('login.html', next=next)


@app.route('/authenticate', methods=['POST',])
def authenticate():
    if request.form['password'] =='alohomora':
        session['logged_user'] = request.form['user']
        flash(f'Usuário {session['logged_user']} logado com sucesso!')
        next_page = request.form['next']
        return redirect(next_page)
    else:
        flash('Usuário não logado')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['logged_user'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

app.run(debug=True)