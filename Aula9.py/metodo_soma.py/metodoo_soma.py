n1 =float(input('Digite um número'))
n2 = float(input('Digigte um número'))
def soma (n1,n2):
    rs_soma = n1 + n2
    return rs_soma

def subtracao (n1,n2):
    rs_sub = n1 + n2
    return rs_sub

def multiplicacao (n1,n2):
    rs_mult = n1 * n2 
    return rs_mult

def divisaoi (n1,n2):
    rs_divit = n1 // n2
    return rs_divisaoi

def divisaof (n1,n2):
    rs_resto = n1 / n2
    return rs_resto

def raiz (n1,n2):
    rs_raiz = n1 ** (1/n2)
    return rs_raiz

print(f'SOMA = {soma(n1,n2)}\nSUBTRAÇÃO = {subtracao(n1,n2)}\nMULTIPLICAÇÃO = {multiplicacao(n1,n2)}\n')

