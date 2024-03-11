
Nome_valido = False
salario_valido = False
bonus_valido = False

while Nome_valido is not True:
    try:
        nome = input("digite seu nome: ")

        #verifica se o nome está vazio
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio")
        
        #verifica se ha numenos no nome
        elif any(char.isdigit() for char in nome):
            raise ValueError("P nome não deve conter numeros")
        else:
            Nome_valido = True
            print("Nome Válido", nome)
    except ValueError as e:
        print(e)

