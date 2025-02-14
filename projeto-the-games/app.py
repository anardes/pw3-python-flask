from flask import Flask #importando pacote do flask

app = Flask (__name__) #carregando flask na variável app

#criando a rota principal do site
@app.route('/')
#criando função no python
def home():
    return '<h1>Meu primeiro site em Flask. Seja bem-vindo!</h1>'

@app.route('/games')
def games():
    return '<h1>Seja bem-vindo à página de games</h1>'
if __name__ == '__main__': #rodando o servidor no localhost, porta 5000
    app.run(host = 'localhost', port=5000, debug = True)
