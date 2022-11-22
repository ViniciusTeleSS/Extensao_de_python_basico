# CALCULADORA

# CABEÇALHO DA CALCULADORA
caractere1 = '-'
qtd_caract = 50

# COLETA DE DADOS
print(caractere1 * qtd_caract)
print('BEM VINDO(A) À CALCULADORA')
print(caractere1 * qtd_caract)

operação = input(
    'Digite o numero da operação que deseja realizar:\n1-SOMA \n2-SUBTRAÇÃO \n3-MULTIPLICAÇÃO \n4-DIVISÃO: ')
print(caractere1 * qtd_caract)

# RESULTADOS
if operação.isnumeric():

    if operação == '1':
        print("VOCÊ ESCOLHEU 'SOMA'")
        print()
        num1 = input('Digite o primeiro número: ')
        num2 = input('Digite o segundo número: ')

        if num1.isnumeric() and num2.isnumeric():
            soma = float(num1) + float(num2)
            print()
            print(f'O resultado da soma entre {num1} e {num2} é {soma:.2f}')
            print(caractere1 * qtd_caract)
        else:
            print('Digite apenas numerais!')

    elif operação == '2':
        print("VOCÊ ESCOLHEU 'SUBTRAÇÃO'")
        print()
        num1 = input('Digite o primeiro número: ')
        num2 = input('Digite o segundo número: ')

        if num1.isnumeric() and num2.isnumeric():
            subtração = float(num1) - float(num2)
            print(
                f'O resultado da subtração de {num2} de {num1} é {subtração:.2f}')
            print(caractere1 * qtd_caract)
        else:
            print('Digite apenas numerais!')
    elif operação == '3':
        print("VOCÊ ESCOLHEU 'MULTIPLICAÇÃO'")
        print()
        num1 = input('Digite o primeiro número: ')
        num2 = input('Digite o segundo número: ')

        if num1.isnumeric() and num2.isnumeric():
            multiplicação = float(num1) * float(num2)
            print(
                f'O resultado da multiplicação de {num1} por {num2} é {multiplicação:.2f}')
            print(caractere1 * qtd_caract)
        else:
            print('Digite apenas numerais!')
    elif operação == '4':
        print("VOCÊ ESCOLHEU 'DIVISÃO'")
        print()
        num1 = input('Digite o primeiro número: ')
        num2 = input('Digite o segundo número: ')

        if num2 == '0':
            print('Divisões por 0 não são válidas')
        else:
            if num1.isnumeric() and num2.isnumeric():
                divisão = float(num1) / float(num2)
                print(
                    f'O resultado da divisão de {num1} por {num2} é {divisão:.2f}')
                print(caractere1 * qtd_caract)
            else:
                print('Digite apenas numerais!')
    else:
        print('Selecione uma opção válida')
else:
    print('Opção inválida, digite o numero de uma das opções.')
