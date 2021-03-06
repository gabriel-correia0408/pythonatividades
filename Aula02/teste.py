from bs4 import BeautifulSoup
import requests

# -- Extração de dados pagina Pokedex Pokemon
# https://www.pokemon.com/br/pokedex

# -- Script criado para obter dados dos pokemons e montar um banco de dados apartir do mesmo


# -- Loop de requests para obter dados de varias paginas
for j in range(1, 10):
    # -- Request recebe a URL da pagina
    pag_html = requests.get(f"https://www.pokemon.com/br/pokedex/{j}").text

    # -- BeuatifulSoap estrai o html da pagina
    soup = BeautifulSoup(pag_html, 'html.parser')


    # print(soup.prettify())

    # -- Defs utilizadas para se obter dados expecificos das tags
    # -- Utilizado metodo de extração por tags que continham class=""
    def title():
        title = str(soup.find_all("div", "pokedex-pokemon-pagination-title"))
        t = title.split('\n')
        t = str(t[2].strip(" "))
        return t


    def type_pokemon():
        type_pokemon = soup.find_all("div", "dtm-type")
        h = str(type_pokemon).split('>')
        h = h[6].strip('</a')
        return h


    def attribute():
        list_attribute = []

        attribute = soup.find_all("span", "attribute-value")
        # -- Altura
        h = str(attribute[0]).strip(' projeto</span class="attribute-value">')
        list_attribute.append(h)
        # -- Peso
        h = str(attribute[1]).strip(' kg</span class="attribute-value">')
        list_attribute.append(h)
        # -- Categoria
        h = str(attribute[3]).replace('<span class="attribute-value">', '')
        h = h.replace('</span>', '')
        list_attribute.append(h)
        # -- Habilidade Principal
        if len(attribute) >= 5:
            h = str(attribute[4]).replace('<span class="attribute-value">', '')
            h = h.replace('</span>', '')
            list_attribute.append(h)
        else:
            h = ''
            list_attribute.append(h)
        # -- Habilidade Secundaria
        if len(attribute) == 6:
            h = str(attribute[5]).replace('<span class="attribute-value">', '')
            h = h.replace('</span>', '')
            list_attribute.append(h)
        else:
            h = ''
            list_attribute.append(h)
        return list_attribute


    def weakness():
        list_weakness = []

        weakness = str(soup.find_all("div", "dtm-weaknesses"))
        a = str(weakness).split('<span>')
        # -- Fraqueza
        h = str(a[1]).split('\n\t')
        h = h[0]
        list_weakness.append(h)
        # -- Fraqueza 2
        if len(a) >= 3:
            t = str(a[2]).split('\n\t')
            t = t[0]
            list_weakness.append(t)
        else:
            t = ''
            list_weakness.append(t)
        return list_weakness


    def description():
        description = str(soup.find_all("p", "version-y"))
        desc = description.split('                  ')
        desc = desc[1].split('\n ')
        desc = desc[0].replace('\n', '')
        return desc


    # -- Chamada das defs e retorno de valores em uma lista
    dados_pokemon = []
    dados_pokemon.append(title())
    dados_pokemon.append(type_pokemon())

    for at in attribute():
        dados_pokemon.append(at)

    for we in weakness():
        dados_pokemon.append(we)

    dados_pokemon.append(description())

    # -- Exibindo na tela valores obtidos
    print(f'-----Pokemon Code: {j}-----')
    for i in dados_pokemon:
        print(i)
    print(f'----------------------------')
