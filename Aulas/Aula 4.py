# TESTE DE LOGIN
login = 'Vinicius'
senha = '123'
contador = 3

while True:

    contador -= 1
    username = input('Digite o seu login: ')
    password = input('Digite sua senha: ')

    if login == username and senha == password:
        print('Login realizado com sucesso!')
        break
    else:
        if contador > 1:
            print(
                f'Login e/ou senha invalido, você tem mais {contador} tentativas')
        elif contador == 1:
            print(
                f'Login e/ou senha invalido, você tem mais {contador} tentativa')
        else:
            print('Acesso bloqueado!')
            break


# TESTE DE TABUADA
'''num = int(input('Digite um numero de 1 a 10 para saber sua tabuada: '))
contador = 1

print(f'Tabuada de {num}:')

while contador <= 10:
    print(f'{num} X {contador} = {num * contador}')
    contador += 1'''

# TESTE DE FATORIAL
'''numero = int(input("Fatorial de: "))

resultado = 1
count = 1

while count <= numero:
    resultado *= count
    count += 1
print(f'{numero}! = {resultado}')'''

'''palavra = list(input("Digite uma palavra: "))

for i in palavra:
    print(i)'''


vendas = [100, 150, 1500, 2000, 120]
vendedores = ['João', 'Felipe', 'Miguel', 'Leandro', 'Vitoria']

for venda in vendas:
    if venda < 1000:
        indice = vendas.index(venda)
        indice_vendedor = vendedores[indice]
        print(
            f'{indice_vendedor} não atingiu a meta pois vendeu {venda} unidades, não recebera bônus.')
    else:
        indice = vendas.index(venda)
        indice_vendedor = vendedores[indice]
        print(
            f'{indice_vendedor} atingiu a meta pois vendeu {venda} unidades, recebera bônus de 15%.')
