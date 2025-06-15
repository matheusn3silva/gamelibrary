from flask import render_template, request, redirect, session, flash, url_for
from jogoteca import app, db
from models import Games, Users

@app.route('/')
def index():
    gameList = Games.query.order_by(Games.id)
    return render_template('list.html', title='Jogos', games=gameList)


# ==========================CREATE GAME==============================
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

    game = Games.query.filter_by(name=name).first()

    if game:
        flash('Jogo já existe!')
        return redirect(url_for('index'))

    new_game = Games(name=name, category=category, console=console)

    db.session.add(new_game)
    db.session.commit()

    return redirect(url_for('index'))

# ==========================EDIT GAME===================================
@app.route('/edit/<int:id>')
def editGame(id):
    if 'logged_user' not in session or session['logged_user'] == None:
        return redirect(url_for('login', next=url_for('editGame')))

    game = Games.query.filter_by(id=id).first()
    return render_template('edit.html', title='Editando Jogo', game=game)

@app.route('/update', methods=['POST'],)
def updateGame():
    game = Games.query.filter_by(id=request.form['id']).first()

    game.name = request.form['name']
    game.category = request.form['category']
    game.console = request.form['console']

    db.session.add(game)
    db.session.commit()

    return redirect(url_for('index'))

# ==========================DELETE GAME=================================


# ==========================LOGIN AUTHENTICATE==========================

@app.route('/login')
def login():
    next = request.args.get('next')
    return render_template('login.html', next=next)


@app.route('/authenticate', methods=['POST',])
def authenticate():
    user = Users.query.filter_by(nickname=request.form['user']).first()

    if user:
        if request.form['password'] == user.password:
            session['logged_user'] = user.nickname
            flash(f'Usuário {user.nickname} logado com sucesso!')
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
