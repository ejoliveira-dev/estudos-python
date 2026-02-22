# Aula 1 de Lógica de Programação.
# Linguagens de Programação.

# Exemplo simples: Imprimir uma mensagem.
print("Olá, mundo!")

# Exemplos extras:
nome = "Éveny"         # armazena texto em uma variável.
print("Olá,", nome,"!")  # imprime variáveis junto com o texto.

def saudar(pessoa):
  """"Retorna uma saudação para a pessoa passada."""
  return f"Olá, {pessoa}! seja bem-vinda(o) ao Colab."
  
print(saudar("Maria"))


# Condicionais.

# Exemplo.
# Vamos definir uma nota.
nota = 8.5

# Verificar a condição.
if nota >=7:
    print("Aprovado")
else:
    print("Reprovado")
    
    
# Imprimir os números de 1 a 100 com um laço for.
for i in range(1, 101): # range(1, 101) gera os números de 1 até 100
   print(i)
   
# -- Ex. Extra. --
# Somar todos os números de 1 até 100.
soma = 0
for i in range(1,101):
    soma += i
print("A soma de 1 a 100 é:", soma)


# Definição da função
def calcular_media(notas):
    """Recebe uma lista de notas e retorna a média"""
    return sum(notas)/len(notas)
    
# -- Ex. de uso. --
notas_aluno = [8.0, 7.5, 9.0, 6.5]
media = calcular_media(notas_aluno)
print("Notas do aluno:", notas_aluno)
print("Média Calculada:", media)
    

  
    
    
    
    
    
    