from datetime import date, timedelta

class Filme:
    def __init__(self, titulo, genero, ano):
        self.titulo = titulo
        self.genero = genero
        self.ano = ano
        self.disponivel = True
        
    def exibir_informacoes(self):
        return f"Título: {self.titulo}, Gênero: {self.genero}, Ano: {self.ano}, Status: {self.disponivel}."
        
    def alugar(self):
        status = "Indisponível" if self.disponivel == False else "Disponível"
        
    def devolver(self):
        status = "Disponível" if self.disponivel == True else "Indisponível"
        
        
        
        
