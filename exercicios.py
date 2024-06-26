# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# try:
#     numero1 = int(input("Digite o primeiro número: "))
#     numero2 = int(input("Digite o segundo número: "))
#     soma_numeros = numero1 + numero2
#     print(f"A soma dos números é de: {soma_numeros}")
# except:
#     print("É preciso inserir um número inteiro")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# numero_usuario = int(input("Digite o número: "))
# calculo_resto = numero_usuario % 5
# print(f"O resto da divisão por 5 é: {calculo_resto}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# numero_1 = int(input("Digite o primeiro número: "))
# numero_2 = int(input("Digite o segundo número: "))
# multiplicacao = numero_1 * numero_2
# print(f"A multiplição dos números é: {multiplicacao}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# try:
#     n1 = int(input("Numero 1: "))
#     n2 = int(input("Numero 2: "))
#     resultado = (n1/n2)
#     print(resultado)
# except ZeroDivisionError:
#     print("integer division or modulo by zero")
# except:
#     print("erro na divisão, por favor confirme os numeros da divisao")

#numero = int(input("Insira um numero inteiro: "))

# if isinstance(numero,int):
#     print("Verdadeiro")
# else:
#     print("Falso")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# numero_usuario = int(input("Digite o número: "))
# numero_ao_quadrado = numero_usuario ** 2
# print(f"O quadrado do número é: {numero_ao_quadrado}")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# numero_1 = float(input("Digite o primeiro número: "))
# numero_2 = float(input("Digite o segundo número: "))
# soma = numero_1 + numero_2
# print(f"A soma dos números é: {soma}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# numero_1 = float(input("Digite o primeiro número:"))
# numero_2 = float(input("Digite o segundo número:"))
# soma = numero_1 + numero_2
# media = soma / 2
# print(f'A média dos números é: {media:.2f}')

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# base = float(input("Informe a base do cálculo: "))
# expoente = float(input("Informe o expoente: "))
# potencia = base ** expoente
# input(f"A potencia de {base} considerando o expoente {expoente} é: {potencia:.2f}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# graus_celsius = float(input("Digite a temperatura em Celsius: "))
# fahrenheit = (graus_celsius * 9/5) + 32
# print(f"{graus_celsius}°C é igual a {fahrenheit}°F")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# import math

# raio_do_circulo = float(input("Digite o raio: "))
# area_do_circulo = math.pi * raio_do_circulo ** 2
# print(f"{area_do_circulo:.2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# minusculo = str(input("Digite qualquer palavra em letra minuscula: "))
# maiusculo = minusculo.upper()
# print(maiusculo)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# maiusculo = str(input("Digite qualquer palavra em letra maiuscula: "))
# minusculo = maiusculo.lower()
# print(minusculo)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# frase = input("Digite uma frase qualquer: ")
# sem_espaco = frase.strip()
# print(sem_espaco)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.da
# data_usuario = input("Insira uma data no formato DD/MM/AAAA: ")
# data_separada = data_usuario.split("/")
# print(data_separada)
# print(f"O primeiro elemento é o: {data_separada[0]}")
# print(f"O segundo elemento é o: {data_separada[1]}")
# print(f"O terceiro elemento é o: {data_separada[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# palavra1 = input("Informe a primeira palavra: ")
# palavra2 = input("Informe a segunda palavra: ")
# concatenacao = palavra1 + " " + palavra2
# print(concatenacao)

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# booleano1 = bool(input("1 - Informe se True or False: "))
# booleano2 = bool(input("2 - Informe se True or False: "))
# resultado = booleano1 and booleano2
# print(f"O resultado do valor booleano para o AND é: {resultado}")

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# booleano1 = bool(input("1 - Informe se True or False: "))
# booleano2 = bool(input("2 - Informe se True or False: "))
# resultado = booleano1 or booleano2
# print(f"O resultado do valor booleano para o OR é: {resultado}")

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# booleano1 = False
# conversao = not booleano1
# resultado = conversao
# print(f"O resultado do valor booleano invertendo ele é: {resultado}")

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# numero1 = input("Informe o primeiro número: ")
# numero2 = input("Informe o segundo número: ")
# resultado = numero1 == numero2
# print(f"O primeiro é igual ao segundo número? A resposta é: {resultado}")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# numero1 = input("Informe o primeiro número: ")
# numero2 = input("Informe o segundo número: ")
# resultado = numero1 != numero2
# print(f"O primeiro é diferente do segundo número? A resposta é: {resultado}")

# #### try-except e if

# 21: Conversor de Temperatura
try:
    graus_celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (graus_celsius * 9/5) + 32
    print(f"{graus_celsius}°C é igual a {fahrenheit}°F")
except ValueError:
    print("O número inserido não é válido, tente novamente.")

# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
