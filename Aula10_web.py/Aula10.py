# Aula 10    20/11/2019
#
#---- web - calculadora

nome_pagina = 'Calculadora nova'
from flask import Flask, render_template, request
from calculo import *

app = Flask(__name__)
@app.route('/')
def inicia():
    return render_template('home.html', titulo=nome_pagina)
  
@app.route('/calcular')
def calcular():
    n1 = int(request.args['numero1'])
    n2 = int(request.args['numero2'])
    rs_soma = soma(n1,n2)
    rs_sub = subtracao(n1,n2)
    rs_mult = multiplicacao(n1,n2)
    rs_divit = divisao_inteira(n1,n2)
    rs_divisaof = divisao_fracionada(n1,n2)
    resultados = {'soma':rs_soma,
                  'subtracao':rs_sub, 
                  'multiplicacao':rs_mult, 
                  'divisao_inteira':rs_divit, 
                  'divisao_fracionada':rs_divisaof}
    #retur f'soma: {n1} e {n2}
    return render_template(
        'resultado.html'
        ,n1 = n1
        ,n2 = n2
        ,resultados = resultados)



        

app.run()