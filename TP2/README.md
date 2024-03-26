# TP2: Conversor de MD para HTML

## Alexandra Santos, a94523

##  Conversor de Lista Markdown para HTML

O programa é um conversor de lista Markdown para HTML. Ele lê um arquivo de texto no formato Markdown e converte-o em HTML.

## Uso

1. Abrair o arquivo 'exemplo.md' no editor de texto.
2. Adicionar o conteúdo Markdown no arquivo.
3. Executar o arquivo 'lista_to_html.py' num ambiente Python, oque criará um arquivo 'exemplo.html' com o conteúdo que foi convertido para HTML.


## Resumo

Conversor de MD para HTML:

- Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto"

        In: # Exemplo

        Out: <h1>Exemplo</h1>

- Bold: pedaços de texto entre "**":

        In: Este é um **exemplo** ...

        Out: Este é um <b>exemplo</b> ...

- Itálico: pedaços de texto entre "*":

        In: Este é um *exemplo* ...

        Out: Este é um <i>exemplo</i> ...

- Lista numerada:

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

- Link: [texto](endereço URL)

        In: Como pode ser consultado em [página da UC](http://www.uc.pt)

        Out: Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>

- Imagem: ![texto alternativo](path para a imagem)

        In: Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...

        Out: Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/>


Como correr o programa:
```
cat examplo.md | python3 tpc2.py
```