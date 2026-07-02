
distancia_km = float(input("Digite a distancia percorrida: "))
combustivel_litros = float (input("Digite o total de combustível gasto: "))
consumo_medio = distancia_km / combustivel_litros

print(f"O consumo médio do seu veículo é de {consumo_medio} km/l.")

# Sistema de Controle de Estoque.

quant_produto = int(input())
quant_produto_min = int(input())

if quant_produto > quant_produto_min:
  print("Produto em estoque!")
elif quant_produto <= quant_produto_min:
  print("Alerta: Estoque baixo. Repor produto!")

nota1 = float(input())
nota2 = float(input())
media = (nota1 + nota2)/2

if media >= 7.0:
  print("Aprovado")
else:
  print("Reprovado")

opcao1 =  "1"
opcao2 = "2"
opcao3 = "3"

print("Escolha uma das opções: ")
print("1- Ver saldo.")
print("2- Realizar saque.")
print("3- Realizar Depósito.")

escolha = str(input())

if escolha == opcao1:
  print("Você selecionou 'Ver saldo'.")
elif escolha == opcao2:
  print("Você selecionou 'Realizar saque'.")
elif escolha == opcao3:
  print("Você selecionou 'Realizar depósito'.")
else:
  print("Opção inválida.")

# gerador de tabuadas.

numero = int(input("Digite um número:"))

print(f"Aqui está a tabuada do número {numero}")

for multiplicador in range(1,11):
  resultado = numero * multiplicador
  print(f"{numero} x {multiplicador} = {resultado}")