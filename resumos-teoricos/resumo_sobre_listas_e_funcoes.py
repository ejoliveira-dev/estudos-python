
# Live 5

# Listas -> um tipo de variável;
# Estrut. de dados que permite manipular uma coleção de elementos/objetos de forma sequencial por meio de um índice (primeiro, segundo...)
# Vant. = Facilidade de poder substituir um grande número de variáveis por uma única variável indexada.

# Índice -> posição de um elemento dentro de uma lista.

lista_notas = [] # Isso aqui é uma lista vazia.

lista_notas = [10, 6, 7, 7, 5, 9] # Isso é uma lista com valores.

#  O primeiro índice de qualquer lista é 0.
lista_notas [0] # Aqui é como acessar a lista do código.
lista_notas [5] # O anterior acessaria o número 10 e esse aqui o número 9.

lista_notas [0] = 9 # Aqui é como atualizar elementos de um grupo.

"""### **COMANDOS/FUNÇÕES PARA USAR EM LISTAS**"""

# .reverse()
# Usado para inverter a ordem de uma lista.
# Não se coloca "print" na frente.

lista_notas = [10, 6, 7, 7, 5, 9]
lista_notas.reverse() # inverteu as posições.

temp_lista = lista_notas.copy() # copiou a lista anterior.
temp_lista.reverse() # agora possui a ordem inicial.

print(lista_notas)
print(temp_lista)

# .sort() ou sorted()
# Usadas para ordenar os valores de uma lista.

# sort() -> mantem a lista ordenada. (alteração permanente na lista, assim como reverse)
# sorted() -> exibe a lista ordenada.

lista_notas = [10, 6, 7, 7, 5, 9]
print(lista_notas.sort()) # (X) -> isso vai exibir "None"

lista_notas.sort()
print(lista_notas)

# -----

lista_notas = [10, 6, 7, 7, 5, 9]
print(sorted(lista_notas)) # aqui é só pra exibição

# .extend() ou +
# Funções usadas para estender uma lista.

# sintaxe -> nome_lista.extend(nome_lista).

lista_notas_a = [10, 6, 7, 7, 5, 9]
lista_notas_b = [1, 4, 8, 3, 1, 4]

lista_notas_a.extend(lista_notas_b)
print(lista_notas_a)

# --- ou -----

lista_notas_a = lista_notas_a + lista_notas_b
print(lista_notas_a)

# Duplicando uma lista
# A nova lista funcionará igual a lista original; qualquer mudança em uma das listas, afetará a outra.

lista_notas = [10, 6, 7, 7, 5, 9]
lista_sincronizada = lista_notas # a lista duplicada sincronizada.
lista_backup = lista_notas.copy() # a lista copiada que não é sincronizada.

lista_sincronizada.extend([1, 2])

print(lista_notas)
print(lista_sincronizada)
print(lista_backup)

# Fatiando a lista (Slicing) - [:]
# Sintaxe -> [indice_inicial : indice_final], onde o valor que estiver no final não será considerado.

lista_notas = [10, 6, 7, 7, 5, 9]
print(lista_notas[-3])

lista_notas_0_3 = lista_notas [0:3]
print(lista_notas_0_3)

# set()
# ordena os valores de uma lista e retira os valores repetidos.

lista_notas = [10, 6, 7, 7, 5, 9]
print(set(lista_notas))

# .count()
# Função usada para contar o número de vezes que um valor aparece na lista.
# Sintaxe -> nome_lista.count(valor)

lista_notas = [10, 6, 7, 7, 5, 9]
print(lista_notas.count(7)) # vai exibir quantas vezes o 7 se repete.

# len()
# Função usada para contar a quantidade de uma coleção (ex.: uma lista ou uma string).
# Sintaxe -> len(coleção)

lista_notas = [10, 6, 7, 7, 5, 9]
print(len(lista_notas)) # ler quantidade de elementos dentro da lista.
print(len("programe.py")) # ler quantidade de letras.

# max() e min()
# imprimem o maior ou o menor valor de uma coleção.

lista_notas = [10, 6, 7, 7, 5, 9]
print(max(lista_notas))
print(min(lista_notas))

print(max("programe.py"))
print(min("programe.py"))

# list()
# Função usada para converter uma string em uma lista

muse = "Park Jimin"
print(list(muse))

# clear()
# Função para limpar todos os valores de uma lista.
# Sintaxe -> nome_lista.clear()

lista_notas = [10, 6, 7, 7, 5, 9]
lista_notas.clear()
print(lista_notas)

# .append()
# Função para adicionar um valor no fim da lista.
# Sintaxe -> nome_lista.append(valor)

lista_notas = []
cont = input("Deseja adicionar valores na lista (S/N)? ")

# laço para inserir notas na lista, acumulando-as na variável soma_notas.
while (cont == "S" or cont == "s"):
  # A parte do len é para exibir a nova posição.
  nota = float(input(f"Informe a {len(lista_notas) + 1}a. nota: "))
  lista_notas.append(nota)
  cont = input("Deseja adicionar mais valores na lista (S/N)? ")

  print(lista_notas)

# ----- Exemplo da cabeça e fácil

bangtan = ["RM", "Jin", "Suga", "J-hope", "Jimin", "V", "Jungkook"]
bangtan.append("BTS")
print(bangtan)

# .insert()
# Função usada para inserir valor em um índice específico da lista.
# Sintaxe -> nome_lista.insert(indice, valor)

bangtan = ["RM", "Jin", "Suga", "J-hope", "V", "Jungkook"]
bangtan.insert(4, "Jimin")
print(bangtan)

# .index()
# Usada para localizar o índice que corresponde a primeira ocorrência de um valor da lista.
# Sintaxe -> nome_lista.index(valor_buscado, inicio_procura, fim_procura)
# inicio_procura e fim_procura são opcionais e correspondem aos indices inicial e final para fazer a procura, respectivamente.


bangtan = ["RM", "Jin", "Suga", "J-hope", "V", "Jungkook"]
print(bangtan)

bias = bangtan.index("J-hope", 0, 5)
print(bias)

bangtan[bias] = "Hoseok"
print(bangtan)

"""Para ***atualizar valores de uma lista*** é necessário:

1. Saber o valor antigo.
2. Verificar se ele existe.
3. Localizar seu índice na lista.
4. Saber qual é o novo valor.
5. Fazer a atualização/atribuição.
6. Verificar se ainda existe outro valor igual para ser atualizado.
"""

bangtan = ["RM", "Jin", "Suga", "J-hope", "Jimin", "V", "Jungkook"]
bangtan[2] = "AgustD"
print(bangtan)

# .pop() ou del

# Excluindo um valor pelo índice.
# comando "del" ou função pop().
# A função pop() retorna o valor que foi retirado da lista.
# Sintaxe ->  nome_lista.pop(indice).
# Atenção: se nenhum indice for especificado a função pop() remove e retorna o último item da lista.

bangtan = ["RM", "Jin", "Suga", "J-hope", "Jimin", "Bangchan", "V", "Jungkook"]
del bangtan[5]
print(bangtan)

# ---------

bangtan = ["RM", "Jin", "Suga", "J-hope", "Jimin", "Bangchan", "V", "Jungkook"]
bangtan.pop(5)

"""Para ***excluir um valor da lista*** deve-se:

1. Verificar se a lista não está vazia.
2. Saber qual valor será excluido.
3. Testar se o valor existe.
4. Fazer a exclusão enquanto houver valor repetido.
"""

# .remove()
# Para excluir um valor da lista.

bangtan = ["RM", "Jin", "Suga", "J-hope", "Jimin", "Bangchan", "V", "Jungkook"]
bangtan.remove("Bangchan")
print(bangtan)

"""### **FUNÇÕES**"""

# Funções correspondem a um trecho de código com objetivo específico que pode ser reutilizado.
# -> facilita o reuso de código.
# -> melhora a compreensão da lógica de programação, aumento da organização do código e facilidade de manutenção do programa.

# Funções Nativas: integradas no Python.

print()
len()
range()

# Funções personalizadas: criadas pelo usuário.
# def indica a definição de uma função.
def nome_da_funcao(parametros): # parametros são opcionais e indicam os valores que a função recebe para processar.
  instrucao 1
  instrucao 2
  ...
  instrucao n
  return valor # return também é opcional e indica o valor que a função devolve após sua execução.

def divisao_limpa():
  v_dividendo = float(input("Informe o dividendo: "))
  v_divisor = float(input("Informe o divisor: "))
  print (v_dividendo / v_divisor)

divisao_limpa() # chamando função; é como a execução ocorre.

# ----------- ou ------------

def divisao(p_dividendo,p_divisor):
	resultado = p_dividendo/p_divisor
	return resultado

# Chamando uma função dentro da outra.

def divisao(p_dividendo,p_divisor):
	resultado = p_dividendo/p_divisor
	return resultado

def divisao_limpa():
	v_dividendo = float(input("Informe o dividendo: "))
	v_divisor = float(input("Informe o divisor: "))
	# aqui a função divisao é chamada dentro da função divisao_limpa
	# perceba que os parâmetros p_dividendo e p_divisor, declarados na especificação
	# da função divisao(p_dividendo,p_divisor), irão assumir os valores das
	# variáveis v_dividendo e v_divisor, respectivamente.
	print (divisao(v_dividendo,v_divisor))

#chamando a função divisao_limpa
divisao_limpa()

# 1) Escopo de variáveis:

# -> Variáveis globais são visíveis em todo o programa, mas seu uso dentro de funções deve ser evitado,
#   pois dificulta a manutenção e pode gerar erros quando nomes se repetem.

# -> Variáveis locais existem apenas dentro da função e são preferidas; quando o nome local é igual ao global,
#   a função usa a variável local. Para alterar uma variável global dentro de uma função, usa-se "global",
#   mas essa prática não é recomendada.

# -> A forma mais indicada é usar parâmetros e retornos, mantendo cada função independente de variáveis externas.

# 2) Delimitação do escopo de funções:

# -> Funções devem ser criadas com um escopo reduzido para facilitar reutilização e reduzir complexidade.

# -> Em vez de criar uma única função grande que lê, calcula e exibe resultados, é melhor dividir em funções menores,
#   como ler_notas(), calcular_media() e exibir_notas_acima_media().

# -> Essa divisão permite reutilizar partes do código em outras funcionalidades, tornando o programa mais organizado,
#   claro e fácil de manter.

# Resumo sobre funções em Python:

# 1. Uma função pode ter vários returns, mas somente um é executado por chamada.
#    O return encerra imediatamente a execução da função e devolve um valor.

# 2. Em Python, o corpo da função precisa estar indentado corretamente.

# 3. Parâmetros:
#    - A ordem importa quando usamos argumentos posicionais.
#    - Podemos trocar a ordem quando usamos argumentos nomeados.
#    - Parâmetros com valores padrão devem vir depois dos sem valor padrão.
#    - Valores padrão são usados quando não enviamos argumentos na chamada.

# 4. Escopo e reutilização:
#    - Funções muito grandes e com escopo amplo tendem a ser menos reutilizáveis.
#    - Dividir uma função grande em funções menores melhora clareza e reaproveitamento.

# 5. Retornos múltiplos:
#    - Uma função pode retornar vários valores separados por vírgulas (tupla).
#    - É possível atribuir cada valor retornado a uma variável separada.
#    - Retornos múltiplos evitam cálculos repetidos, como somar uma lista duas vezes.

# 6. Exemplos conceituais:
#    - calcular_media(lista): soma os valores e divide pelo total.
#    - exibir_notas_acima_media(media, lista): mostra apenas notas maiores que a média.
#    - calcular_soma_media(lista): retorna soma e média simultaneamente.

# Este conjunto de ideias forma a base para escrever funções mais claras,
# eficientes, organizadas e reutilizáveis em Python.
