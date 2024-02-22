import re

def lista_to_html(lista):
    # Converter cabeçalhos
    lista = re.sub(r'^#\s+(.*)$', r'<h1>\1</h1>', lista, flags=re.MULTILINE)
    lista = re.sub(r'^##\s+(.*)$', r'<h2>\1</h2>', lista, flags=re.MULTILINE)
    lista = re.sub(r'^###\s+(.*)$', r'<h3>\1</h3>', lista, flags=re.MULTILINE)

    # Converter negrito
    lista = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', lista)

    # Converter itálico
    lista = re.sub(r'\*(.*?)\*', r'<i>\1</i>', lista)

    # Converter lista numerada
    lista = re.sub(r'^(\d+\.\s*)(.*)', r'<ol><li>\2</li></ol>', lista, flags=re.MULTILINE)

    # Converter link
    lista = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', lista)

    # Converter imagem
    lista = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', lista)

    return lista

with open('exemplo.md', 'r') as file:
    lista = file.read()

html = lista_to_html(lista)

with open('exemplo.html', 'w') as file:
    file.write(html)