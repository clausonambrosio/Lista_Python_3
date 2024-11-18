class Filme:
    def __init__(self, titulo, genero, ano):
        self.titulo = titulo
        self.genero = genero
        self.ano = ano
        self.disponivel = True
        
    def exibir_informacoes(self):
        return f"Título: {self.titulo}, Gênero: {self.genero}, Ano: {self.ano}, Status: {self.disponivel}."
        
    def alugar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"Filme '{self.titulo}' alugado com sucesso.")
        else:
            print(f"Filme '{self.titulo}' indisponível.")
        
    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"Filme '{self.titulo}' devolvido com sucesso.")
        else:
            print(f"Filme '{self.titulo}' já está disponível.")
            
    def __str__(self):
        return f"Título: {self.titulo:20} | Gênero: {self.genero:10} | Ano: {self.ano:4} | Disponível: {self.disponivel}"

    def alugar_filme(filmes):
        titulo = input("Digite o título do filme que deseja alugar: ")
        for filme in filmes:
            if filme.titulo == titulo:
                filme.alugar()
                return
        print(f"Filme '{titulo}' não encontrado.")
                
    def devolver_filme(filmes):
        titulo = input("Digite o título do filme que deseja devolver: ")
        for filme in filmes:
            if filme.titulo == titulo:
                filme.devolver()
                return
        print(f"Filme '{titulo}' não encontrado.")
    
    def listar_filmes(filmes):
        if not filmes:
            print("Não há filmes cadastrados.")
        else:
            for filme in filmes:
                print(filme)
                
filmes = []  # Lista para armazenar os filmes

def menu():
    while True:
        print("1 - Cadastrar filme")
        print("2 - Alugar filme")
        print("3 - Devolver filme")
        print("4 - Listar filmes")
        print("5 - Sair")

        opcao = int(input('Digite a opção: '))

        if opcao == 1:
            titulo = input("Digite o título do filme: ")
            genero = input("Digite o gênero do filme: ")
            ano = int(input("Digite o ano de lançamento: "))
            filme = Filme(titulo, genero, ano)
            filmes.append(filme)
            print("Filme cadastrado com sucesso!")
        elif opcao == 2:
            Filme.alugar_filme(filmes)
        elif opcao == 3:
            Filme.devolver_filme(filmes)
        elif opcao == 4:
            Filme.listar_filmes(filmes)
        elif opcao == 5:
            print("Até logo!!!")
            break
        else:
            print("Opção inválida.")
            
if __name__ == "__main__":
    menu()
    
