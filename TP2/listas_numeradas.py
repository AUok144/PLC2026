import re


'''
TPC2: Criar em Python um conversor de MarkDown para HTML lista numerada:

In:
1. Primeiro item
2. Segundo item
3. Terceiro item

Out:
<ol>
<li>Primeiro item</li>
<li>Segundo item</li>
<li>Terceiro item</li>
</ol>

'''


# a lista é iniciada com <ol>;
# cada linha que começa por um número )seguido de ponto e espaço) é um item da lista;
# cada item é envolvida por <li> item </li>;
# a lista termina com um </ol>.


def conversor_lista_numerada(txt):

    # separa o input em linhas para facilitar a conversão
    linhas = txt.split("\n") 

    item = re.compile(r'\d+\.\s+(.*)')
    # identifica itens no padrão:
    # \d+   -> um ou mais algarismos
    # \.    -> ponto
    # \s+   -> um ou mais espaços
    # (.*)  -> texto do item

    html = [] # lista que devolve no fim
    aberta = False 

    for linha in linhas:
        i = item.match(linha)

        # se a linha for um item 
        if i:

            # inicia a lista se for o primeiro item
            if not aberta:
                html.append("<ol>")
                aberta = True

            # adiciona o item à lista
            html.append("<li>" + i.group(1) + "</li>")

        else:

            # se houver lista aberta, fecha
            if aberta:
                html.append("</ol>")
                aberta = False

            # adiciona o item original
            html.append(linha)

    # marca fecho à lista
    if aberta:
        html.append("</ol>")

    # retorna a lista convertida numa única string
    return "\n".join(html)


# teste
txt = """1. Primeiro item
2. Segundo item
3. Terceiro item"""

print(conversor_lista_numerada(txt))

txt2 = """1. 123
2. 456.7
3. -134
4. 1.234E+02"""

print(conversor_lista_numerada(txt2))