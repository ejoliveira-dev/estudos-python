
a = int(input()) # Troca de valores
b = int(input()) # Escreva um programa que permute (troque) o valor de duas variáveis inteiras.

a, b = b, a

print(f"Valor de a após permutação: {a}")
print(f"Valor de b após permutação: {b}")

custo = float(input()) # Qual o meu lucro?
venda = float(input()) # Escreva um programa que, a partir de um valor de custo e de um valor de venda, mostre o valor do lucro obtido com a venda do produto.

lucro = venda - custo

print(f"O lucro obtido foi R$ {lucro:.2f}.")

nome = str(input("Digite seu nome: ")) # Idade em meses e dias.
idade_anos = int(input("Digite sua idade: ")) # Escreva um programa que receba o nome de uma pessoa e sua idade em anos. O programa deve calcular e exibir a idade da pessoa em meses e dias.

idade_meses = idade_anos * 12
idade_dias = idade_anos * 365

print(f"{nome} tem {idade_anos} anos ou {idade_meses} meses ou ainda {idade_dias} dias!")

altura = float(input()) # Calcule o volume de um cilindro.
raio = float (input())
pi = 3.14
volume_total =  pi * (raio ** 2) * altura

print(f"O volume do cilindro que tem {altura} de altura e {raio} de raio é igual a {volume_total:.2f}")

temperatura_celsius = float(input())  # Crie um programa que receba uma temperatura em Celsius e exiba a temperatura lida usando as escalas Kelvin (K) e Fahrenheit (F).
temperatura_kelvin = temperatura_celsius + 273
temperatura_fahrenheit = 1.8 * temperatura_celsius + 32

print(f"Temperatura em Kelvin: {temperatura_kelvin:.2f}K")
print(f"Temperatura em Fahrenheit: {temperatura_fahrenheit:.2f}ºF")

# Escreva um programa que leia as 2 notas de um aluno em uma disciplina, depois exiba quantos pontos o aluno ficou distante da nota 10 para cada avaliação, sua média e quantos pontos a média do aluno ficou distante da nota 10.

nota_1 = float(input())
nota_2 = float(input())
distancia_para_10_1 = 10 - nota_1
distancia_para_10_2 = 10 - nota_2
media = (nota_1 + nota_2) / 2
distancia_media_para_10 = 10 - media

print(distancia_para_10_1)
print(distancia_para_10_2)
print(media)
print(distancia_media_para_10)

# Escreva um programa que, leia um valor de custo e o percentual de lucro desejado, e na sequencia mostre o valor final do produto;

valor_custo = float (input())
percentual_lucro = float (input())
valor_percentual_lucro = valor_custo * (percentual_lucro / 100)
valor_final = valor_custo + valor_percentual_lucro

print(f"Valor final do produto: R$ {valor_final:.4f}.")

# Escreva um programa que leia o salário de uma pessoa, quantas horas ela trabalha por dia e quantos dias ela trabalhou no mês. Em seguida, calcule e exiba quanto essa pessoa recebe por hora.

salario = float(input())
horas_por_dia = int(input())
dias_trabalhados = int(input())
valor_salario_hora = (salario / dias_trabalhados) / horas_por_dia

print(f"Eu recebo uma mixuruca de R$ {valor_salario_hora:.1f} por hora trabalhada.")

# Faturamento de um show.

total_ingressos = int(input())
ingresso_meia_percentual = int(input())
valor_ingresso_inteira = float(input())
total_meia = (total_ingressos * ingresso_meia_percentual) // 100
total_inteira = total_ingressos - total_meia
faturamento_meia = (valor_ingresso_inteira / 2) * total_meia
faturamento_inteira = valor_ingresso_inteira * total_inteira
faturamento_total = faturamento_meia + faturamento_inteira

print(f"Quantidade de ingressos meia-entrada: {total_meia}")
print(f"Quantidade de ingressos inteiros: {total_inteira}")
print(f"Faturamento com meia-entrada: R${faturamento_meia:.2f}")
print(f"Faturamento com inteira: R${faturamento_inteira:.2f}")
print(f"Faturamento total: R${faturamento_total:.2f}")
