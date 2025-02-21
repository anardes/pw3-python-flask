from flask import Flask, render_template#importando pacote do flask

app = Flask (__name__, template_folder='views') #carregando flask na variável app

#criando a rota principal do site
@app.route('/')
#criando função no python
def home():
    return render_template('index.html')

@app.route('/games')
#criando função no python
def games():
    titulo='CS-GO'
    ano=2012
    categoria='FPS Online'
    jogadores=['iruah', 'davi_lambari', 'edsongf1', 'kioto', 'jujudopix']
    jogos=['subway surfers', 'free fire', 'fortnite', 'cyberpunk', 'pou', 'my talking tom', 'plant vs zombie']
    return render_template('games.html',
                           titulo=titulo,
                           ano=ano,
                           categoria=categoria,
                           jogadores=jogadores,
                           jogos=jogos)

if __name__ == '__main__': #rodando o servidor no localhost, porta 5000
    app.run(host = 'localhost', port=5000, debug = True)
