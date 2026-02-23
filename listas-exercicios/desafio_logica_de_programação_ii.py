# Desafio de Lógica de Programação.

# Objeto "Livro":

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


