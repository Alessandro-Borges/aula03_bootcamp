# Exericio 6, contagem de palavra em textos
    
texto = "Hoje e nossa segunda aula do bootcamp, bootcamp de python"

# dicionario, coluna e 1 atributo

palavras = texto.split(" ")

contagem_de_palavras  = {}

for palavra in palavras:
    if palavra in contagem_de_palavras:
        contagem_de_palavras[palavra] =+1
    else:
        # add a element in a dict python
        contagem_de_palavras[palavra] = 1
print(contagem_de_palavras)