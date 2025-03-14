from flask import render_template, request
jogadores=['iruah', 'davi_lambari', 'edsongf1', 'kioto','black_butterfly', 'jujudopix']
gamelist=[{'Título' :'CS-GO', 'Ano': 2012, 'Categoria' : 'FPS online'}]
console=[{'Título' : 'PS 5', 'Preço' : 4.332, 'País' : 'Japão'}]
        
def init_app(app):
    @app.route('/')
#criando função no python
    def home():
        return render_template('index.html')

    @app.route('/games', methods = ['GET','POST'])
#criando função no python
    def games():
        game= gamelist[0]
        
        if request.method == 'POST':
            if request.form.get('jogador'):
                jogadores.append(request.form.get('jogador'))
        return render_template('games.html',
                           game = game,
                           jogadores=jogadores,)
    @app.route('/cadgames')
    def cadgames():
        
        if request.method == 'POST':
            if request.form.get('titulo') and request.form.get('ano') and request.form.get('categoria'):
                gamelist.append({'Título' : request.form.get('titulo'), 'Ano': request.form.get('ano'), 'Categoria' : request.form.get ('categoria')})
        return render_template('cadgames.html', gamelist=gamelist)
    @app.route('/cadconsole')
    def cadconsole():
        
        if request.method == 'POST':
            if request.form.get('titulo') and request.form.get('preço') and request.form.get('pais'):
                console .append({'Título' : request.form.get('titulo'), 'Preço' : request.form.get('preço'), 'País' : request.form.get('pais')})
        return render_template('cadconsole.html', consoless=console)
                