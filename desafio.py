# 1) Solicita ao usuário que digite seu nome

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

# 4) Calcule o valor do bônus final

# 5) Imprima cálculo do KPI para o usuário

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

name = input("Type your name: ")
salary = float(input("Type your salary: "))
bonus = float(input("Type your bonus: "))
CONSTANTE_BONUS = 1000

final_bonus = CONSTANTE_BONUS + salary * bonus 

print(f'###============###\nMr./Mrs. {name},\nYour salary is: {salary}\nAnd your final bonus is: {final_bonus}\n###============###')
