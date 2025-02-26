# Exercício 1: Crie programa que o usuário digita o seu nome e retorna o número de caracteres
# print(len(input("Digite seu nome: ")))

# Exercício 2: Criar um programa onde o usuário digite dois valores e apareça a soma
""" qt_numbers_sum = int(input("Type the number values that need to be added: "))

list = []

for i in range(qt_numbers_sum):
    added_value = int(input("Type the values of sum: "))
    list.append(added_value)

print(f'This is the value of sum: {sum(list)}') """

# Exercício 03: Refatore o exercício 01 atribuindo variáveis.
name = input("Type your name: ")
qt_characters = len(name)

print(f'The characters numbers is: {qt_characters}')