""" alfabeto = []

for i in range(97, 123):
    alfabeto.append(chr(i))
print(alfabeto) """

""" entrada = list(input("Digite uma mensagem: "))
saida = []


for letra in entrada:
    num = ord(letra)
    if num >= 97 and num <= 122:
        num += 3
        saida.append(chr(num))
    else:
        saida.append(chr(num))
print(saida) """

""" lista = [1, 2, 2, 2, 3, 4, 5, 5, 6, 6, 6, 6, 7, 8, 9, 2]

len_lista = len(lista)
set_lista = len(set(lista))

print(f'A lista tem {len_lista} elementos e o set tem {set_lista} elementos')
 """

""" receita = {
    'jan': 100,
    'fev': 120,
    'mar': 100
}

receita['abr'] = 300
novo_elemento = {'mai': 250}
receita.update(novo_elemento)


for chave,valor in receita.items():
    print(f'{chave} : {valor}') """

""" acessos = {

    'Vinicius': '123',
    'Camilla': '456',
    'Claudio': '789'
}

username = input("Digite seu login: ")
password = input("Digite sua senha: ")

for login, senha in acessos.items():
    if login == username and senha == password:
        print(f'Bem-vindo {login}')
        break
    else:
        print('Usuario ou senha inválidos')
        break  """

""" banco_dados = {

    'joao': '123',
    'felipe': '456',
    'miguel': '789'
}

username = input("Login: ").casefold()
password = input("Senha: ").casefold()

for login, senha in banco_dados.items():

    if login == username and senha == password:
        print(f'Bem-vindo {login}')

    else:
        print('Usuário ou senha inválidos') """
