## TPC2: Conversor de Markdown para HTML — Listas Numeradas

## Autor
Chen Yuqing - A108397

<img src="../imagens/foto.jpg" width="120">

## Resumo
Neste trabalho foi desenvolvido em Python um conversor simples de listas numeradas em Markdown para HTML.

O programa identifica linhas no formato "número. texto" através de uma expressão regular. Quando encontra o primeiro item, abre uma lista HTML com a tag `<ol>`, converte cada elemento para `<li>...</li>` e fecha a lista com `</ol>`.

Para reconhecer os itens foi utilizada a expressão regular `\d+\.\s+(.*)`, que identifica um ou mais dígitos, seguidos de um ponto, espaço e do conteúdo do item.

## Lista de resultados
[resolução](listas_numeradas.py)
