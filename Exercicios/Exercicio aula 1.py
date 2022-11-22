# 1. Usuário entra com 3 números (x, y e z)
# 2. Imprime na tela x + y
# 3. Imprime na tela x elevado a z
# 4. Imprime a subração x - y - z

x = float(input("Digite um número: "))
y = float(input("Digite um segundo número: "))
z = float(input("Digite terceiro número: "))

somaxy = x + y
xelevado = x ** z
subtração = x - y - z

print(f"A soma de {x:.2f} com {y:.2f} é: {somaxy:.2f}")
print(f"{x} elevado a {z} é: {xelevado} ")
print(f"E a subtração de {x},{y} e {z} é: {subtração}")
