from flask import Flask, render_template, request

app = Flask(__name__)

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return a

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operacao = request.form['operacao']

    if operacao == 'soma':
        resultado = soma(num1, num2)
    elif operacao == 'subtracao':
        resultado = subtracao(num1, num2)
    elif operacao == 'multiplicacao':
        resultado = multiplicacao(num1, num2)
    elif operacao == 'divisao':
        resultado = divisao(num1, num2)

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
