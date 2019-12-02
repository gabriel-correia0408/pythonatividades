from flask import Flask
from faixa import

app = Flask(__name__)


@app.route('/lista')
def lista_fixas():
    return render_template("lista.html", nome = 'lista de faixas')


app.run()