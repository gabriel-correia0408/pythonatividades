# Aula 18 - 03-11-2019

# interação de lista com o for

# Usando o comando for vamos fazer uma interação de varialvel tipo coleção. A interação é (simplificadamente) 
# percorer toda a variavel e isolar seu valores.

# 1.1 Com a seguinte lista, use o for para interar esta tupla  e apresentar (usando o f-string) O nome da cerveja, 
# tipo da cerveja, o IBU da cerveja e o preço dela.

cerveja = (('marca', 'tipo', 'ibu','preço'),
           ('Skol','IPA','ultra-leve',3.50),
           ('Brahma','lager','leve/media',3.45),
           ('Kaiser','Americam Larger','leve',2.35),
           ('Sol','larger mão','agua',1.19)
          )

cabe = cerveja[0]
# (('marca', 'tipo', 'ibu','preço'),

dados = cerveja[1:]
# ('Skol','IPA','ultra-leve',3.50),
#            ('Brahma','lager','leve/media',3.45),
#            ('Kaiser','Americam Larger','leve',2.35),
#            ('Sol','larger mão','agua',1.19)


for daddos_cerveja in dados:
    for i in range (4):
        print(f"{cabe[i]} - {daddos_cerveja[i]}")