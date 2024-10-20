from flask import Flask, render_template

app = Flask(__name__)

# Rota para a página principal (Cenário Atual)
@app.route('/')
def index():
    return render_template('paginas_calculadora.html')

# Rota para a página do Simples Nacional
@app.route('/simples_nacional')
def simples_nacional():
    return render_template('simples_nacional.html')

# Inicia o servidor
if __name__ == '__main__':
    app.run(debug=True)
