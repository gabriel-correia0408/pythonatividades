n1 = float(input('Dgite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
rs = (n1+n2+n3+n4)/4
if rs > 7:
    print(f'APROVADO, com média de: {rs}')
else:
  print(f'REPROVADO, com média de: {rs}')

if n1 > n2 and n1 > n3 and n1 > n4:
      print(f'A maior nota é {n1}')

if n2 > n1 and n2 > n3 and n2 >  n4:
    print (f'A maior nota é {n2}')

if n3 > n1 and n3 > n2 and n3 > n4:
    print(f'A maoir nota é {n3}')


if n4 > n1 and n4 > n2 and n4 > n3:
    print(f'A maior nota é {n4}') 

if n1 < n2 and n1 < n3 and n1 < n4:
      print(f'A menor nota é {n1}')

if n2 < n1 and n2 < n3 and n2 <  n4:
    print (f'A menor nota é {n2}') 

if n3 < n1 and n3 < n2 and n3 < n4:
    print(f'A menor nota nota é {n3}')

if n4 < n1 and n4 < n2 and n4 < n3:
    print(f'A menor nota é {n4}')        
      