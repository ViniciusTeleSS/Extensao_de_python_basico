# Faça um Programa que leia 1 número e, em seguida, informe ao usuário se o número é: Par ou ímpar e Positivo ou negativo

n1 = int(input("Digite um numero: "))
parimpar = n1 % 2

if parimpar == 0:
    print("O numero é par")
else:
    print("O numero é impar")

if n1 >= 0:
    print("O numero é positivo")
else:
    print("O numero é negativo")
