# Aluno(a): Éveny Janiely O. Melo.
# Exercício/Desafio: Classe Livro e Classe Carro.
# Disciplina: Lógica de Programação II.


# Classe Livro:


class Livro: 
    def __init__(self, titulo, autor, paginas, leitor):
        self.titulo = titulo 
        self.autor = autor 
        self.paginas = paginas 
        self.leitor = leitor 
        self.atual_pagina = 0
    
    def apresentar(self): 
        return f"O livro que {self.leitor} está lendo, {self.titulo}, escrito por {self.autor}, tem {self.paginas} páginas!" 
        
    def ler_pagina(self): 
        self.atual_pagina = round(self.paginas * 0.11)
        return f"No primeiro dia, {self.leitor} leu até a página {self.atual_pagina}." 
        
    def semana_leitura(self): 
        self.atual_pagina = round(self.paginas * 0.75)
        return f"Em uma semana, já tinha lido {self.atual_pagina} páginas desse livro." 
    
    def termino_leitura(self): 
        return f"Em menos de um mês, {self.leitor} já tinha terminado de ler {self.titulo}!"
        
livro1 = Livro("Amêndoas","Won-Pyung Sohn", 286, "Luara") 
livro2 = Livro("A Menina Que Roubava Livros", "Markus Zusak", 480, "Isaac") 
livro3 = Livro("Querido Evan Hansen", "Val Emmich", 336, "Bryan") 

print(livro1.apresentar()) 
print(livro1.ler_pagina()) 
print(livro1.semana_leitura()) 
print(livro1.termino_leitura()) 

print()

print(livro2.apresentar()) 
print(livro2.ler_pagina()) 
print(livro2.semana_leitura()) 
print(livro2.termino_leitura()) 

print()

print(livro3.apresentar()) 
print(livro3.ler_pagina()) 
print(livro3.semana_leitura())
print(livro3.termino_leitura())


# Classe Carro (Outros atributos/métodos):


class Carro: 
    def __init__(self, tipo, distancia, consumo, pessoa):
        self.tipo = tipo
        self.distancia = distancia
        self.consumo = consumo
        self.pessoa = pessoa
        self.gasto_gasolina = 6.00
        
    def apresentar(self):
        if self.tipo == "o carro do ano" or self.tipo == "um carro":
          return f"Este é {self.pessoa} e ele tem {self.tipo}."
        else:
          return f"Este é {self.pessoa} e ele tem que correr para não perder ônibus todos os dias."
          
    def vida(self):
        if self.consumo == 0:
         return f"Está sempre passando altos perrenges por morar longe do trabalho."
         
        litros_usados = self.distancia / self.consumo
        gasto_total = litros_usados * self.gasto_gasolina
        
        if gasto_total >= 60:
          return f"Ele gasta muito todos os dias só em gasolina, mas ele não liga, ele gosta de esbanjar seu carro."
        else:
          return f"Infelizmente, ele tem que trabalhar e por morar longe, acaba gastando na ida e na volta."

carro1 = Carro("o carro do ano", 120, 10, "Maurício")
carro2 = Carro("um carro", 80, 18, "Carlos")
carro3 = Carro("Não tem", 150, 0, "Jonathan")

print(carro1.apresentar())
print(carro1.vida())

print()

print(carro2.apresentar())
print(carro2.vida())

print()

print(carro3.apresentar())
print(carro3.vida())
