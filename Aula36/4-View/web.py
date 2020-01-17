from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_temlate('index.html', titulo_app = nome)
 

app.run(debug=true, pot=80)