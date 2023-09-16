from flask import Flask, render_template, request, redirect, url_for
from PIL import Image

app = Flask(__name__)

contatos = {
    '12345': {
        'nome': 'João',
        'telefone': '123-456-7890',
        'imagem': 'images/joao.jpg'
    },
    '67890': {
        'nome': 'Maria',
        'telefone': '987-654-3210',
        'imagem': 'maria.jpg'
    }
}


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/buscar', methods=['POST'])
def buscar():
  numero = request.form['numero']
  if numero in contatos:
    contato = contatos[numero]
    return render_template('resultado.html', contato=contato)
  else:
    return render_template('contato_inexistente.html')


if __name__ == '__main__':
  app.run(debug=True)
