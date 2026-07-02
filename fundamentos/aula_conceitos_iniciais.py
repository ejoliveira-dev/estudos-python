# Aula/live sobre Python.
# Descomplicando Programação com Python.

print('Olá, estranho')
# Exibe o texto na tela.

c = 2 
print(c)
# A Classe recebe um dado/atributo.

print(type(c))
# Diga o tipo de dado que está em "c".

b = "Louise"
print(type(b))
# Para dados com letras, as aspas são usadas.

x = 10
y = 17
print(x == y)
# dados booleanos: tipos de dados lógicos e só podem ter dois valores possíveis: true ou false.

# + = soma; - = subtração; * = multiplicação; / = divisão.
# exponenciação = **; divisão inteira = //; para dizer o resto da divisão = %.
# Operadores aritméticos.

n = 6 ** 2
print(n)

s = n // 2
print(s)

d = 10%3
print(d)

# Operadores Relacionais simples:
# >, <,==.

# Operadores Relacionais compostos:
# =>, <=,!= (diferente de).

a = 9
p = 5
print(a >= p)

numero = 17
print(f"O número {numero} é impar.")
# f = format.

# Função input.

nome = input("Digite seu nome:")
print(f"Seu nome é {nome}.")

idade = input("Digite sua idade:")
print(f"Você tem {idade} anos.")
print(type(idade))

idade = int(input("Digite sua idade:"))
print(f"Você tem {idade} anos.")
print(type(idade))
# Assim ele reconhece o dado como inteiro.

# Tipo de dado FLoat/Real.
peso = float (input("Digite seu peso:"))
print(f"Você pesa  {peso}KGs.")
print(type(peso))

# Estruturas de Condições.
numero = int(input("Digite um número:"))
if numero % 2 == 10:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é impar.")

# É importante seu código não ter um erro de identação. (espaços faltando, colunar alinhadas...)

num = int (input("Digite seu peso:"))
if num > 0:
    print("Este número é positivo")
elif num == 0:
    print("Este número é neutro")

else:
    print("Este número é negativo")

# Estruturas de condições alinhadas e o ELIF.
# Comando alternativo de IF/ELSE.

# Operadores Lógicos: and, or, not; Função Range(); e operadores in, not in.

resposta = int(input("Qual a sua idade?:"))
if resposta >=18 and resposta <=65:
    print("Você é obrigado a votar")
else:
    print("Você não é obrigado a votar!")

print("1. Idoso")
print("2. Gestante")
print("3. Cadeirante")
print("4. Nenhum desses")
resp=int(input("Você é:"))
if (resp == 1) or (resp == 2) or (resp == 3):
    print("Você tem direiro a fila prioritária.")
else:
    print("Você não tem direito a nada. Vá pra fila!")
   

