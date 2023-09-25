#Guilherme S. de Oliveira - 32126344
#Lucas G. C. L. Martins   - 32154488
from art import *


#classe para poder armazenar os vertices com nome, generos e atores
class Vertice:
    def __init__(self, nome, generos, atores):
        self.nome = nome
        self.generos = list(generos)
        self.atores = list(atores)

#classe do grafo
class Grafo:
    #funcao de inicializador do grafo
    def __init__(self):
        self.vertices = []
        self.matriz_adjacencia = []
    #funcao de adicionar vertice
    def adicionar_vertice(self, vertice):
        self.vertices.append(vertice)
        for linha in self.matriz_adjacencia:
            linha.append(0)
        nova_linha = [0] * len(self.vertices)
        self.matriz_adjacencia.append(nova_linha)
    #funcao de adicionar vertice
    def adicionar_aresta(self, vertice1, vertice2, peso):
        index1 = self.vertices.index(vertice1)
        index2 = self.vertices.index(vertice2)
        self.matriz_adjacencia[index1][index2] = peso
        self.matriz_adjacencia[index2][index1] = peso
    #funcao de imprimir a matriz de adjacencia
    def imprimir_matriz_adjacencia(self):
      for linha in self.matriz_adjacencia:
            print(linha)

    #funcao que procura os filmes por genero
    def consultar_filmes_por_genero(self, genero):
        filmes_por_genero = []
        for vertice in self.vertices:
            if genero in vertice.generos:
                filmes_por_genero.append(vertice)
        return filmes_por_genero
    #funcao que procura os filmes por ator
    def consultar_filmes_por_ator(self, ator):
        filmes_por_ator = []
        for vertice in self.vertices:
            if ator in vertice.atores:
                filmes_por_ator.append(vertice)
        return filmes_por_ator
    #funcao de remover vertice
    def remover_vertice(self, vertice):
        if vertice in self.vertices:
            indice = self.vertices.index(vertice)
            del self.vertices[indice]
            for linha in self.matriz_adjacencia:
                del linha[indice]
            del self.matriz_adjacencia[indice]
            print(f"Vértice '{vertice.nome}' removido do grafo.")
        else:
            print("Vértice não encontrado.")

    #funcao de remover arestas
    def remover_aresta(self, vertice1, vertice2):
        index1 = self.vertices.index(vertice1)
        index2 = self.vertices.index(vertice2)
        if self.matriz_adjacencia[index1][index2] > 0:
            self.matriz_adjacencia[index1][index2] = 0
            self.matriz_adjacencia[index2][index1] = 0
            print(f"Aresta entre '{vertice1.nome}' e '{vertice2.nome}' removida.")
        else:
            print("Aresta não encontrada.")

    #funcao de que verifica conectividade
    def verificar_conectividade(self):
        visitados = set()  

        def dfs(vertice):
            visitados.add(vertice)
            for i, adjacente in enumerate(self.vertices):
                if self.matriz_adjacencia[self.vertices.index(vertice)][i] > 0 and self.vertices[i] not in visitados:
                    dfs(adjacente)
        if self.vertices:
            dfs(self.vertices[0])
        conectado = len(visitados) == len(self.vertices)

        return conectado
    #funcao de criar grafo reduzido
    def criar_grafo_reduzido(self):
      grafo_reduzido = Grafo()
      for vertice in self.vertices:
          grafo_reduzido.adicionar_vertice(vertice)
      for i in range(len(self.vertices)):
          for j in range(i + 1, len(self.vertices)):
              if self.matriz_adjacencia[i][j] > 0:
                  vertice1 = self.vertices[i]
                  vertice2 = self.vertices[j]
                  peso = self.matriz_adjacencia[i][j]
                  if self.ha_caminho(vertice1, vertice2):
                      grafo_reduzido.adicionar_aresta(vertice1, vertice2, peso)
  
      return grafo_reduzido
    #funcao que verifica os caminhos para o grafo reduzido
    def ha_caminho(self, origem, destino):
        visitados = set() 
    
        def dfs(vertice):
            visitados.add(vertice)
            for i, adjacente in enumerate(self.vertices):
                if self.matriz_adjacencia[self.vertices.index(vertice)][i] > 0 and self.vertices[i] not in visitados:
                    dfs(adjacente)
    
        dfs(origem)
    
        return destino in visitados
#funcao para ler os dados dos arquivos
def ler_filmes_e_generos(arquivo):  
  n = int(arquivo.readline().strip())
  atores=[0]*2
  generos=[0]*2
  for _ in range(n):
    linha = arquivo.readline().strip().split(',')
    generos[0]=linha[1]
    generos[1]=linha[2]
    atores[0]=linha[3]
    atores[1]=linha[4]
    vertice = Vertice(linha[0], generos, atores)
    grafo.adicionar_vertice(vertice)
  n = int(arquivo.readline().strip())
  print(n)
  for _ in range(n):
    linha = arquivo.readline().strip().split(',')
    filme1=linha[0]
    filme2=linha[1]
    peso=int(linha[2])
    vertice1 = next((v for v in grafo.vertices if v.nome == filme1), None)
    vertice2 = next((v for v in grafo.vertices if v.nome == filme2), None)
    if vertice1 and vertice2:
      grafo.adicionar_aresta(vertice1, vertice2, peso)
      print(f"Aresta entre '{filme1}' e '{filme2}' adicionada com peso {peso}.")
    else:
      print("Um ou ambos os vértices não foram encontrados.")

#funcao para salvar os grafos no arquivo
def salvar_grafo_em_txt(grafo, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(f"{len(grafo.vertices)}\n")
        for vertice in grafo.vertices:
            arquivo.write(f"{vertice.nome},{','.join(vertice.generos)},{','.join(vertice.atores)}\n")
        
        arestas = []
        for i in range(len(grafo.vertices)):
            for j in range(i+1, len(grafo.vertices)):
                if grafo.matriz_adjacencia[i][j] > 0:
                    filme1 = grafo.vertices[i].nome
                    filme2 = grafo.vertices[j].nome
                    peso = grafo.matriz_adjacencia[i][j]
                    arestas.append(f"{filme1},{filme2},{peso}")
        
        arquivo.write(f"{len(arestas)}\n")
        for aresta in arestas:
            arquivo.write(f"{aresta}\n")

#funcao para imprimir todos os filmes
def imprimir_dados_filmes(grafo):
  for vertice in grafo.vertices:
        print(vertice.nome)
        print(f"Generos = {vertice.generos}")
        print(f"Atores = {vertice.atores}")
        print()  # Adiciona uma linha em branco para separar os dados de cada film


#funcao para verificar os filmes parecidos
def filmes_conectados(grafo, nome_filme):
    vertice_escolhido = next((v for v in grafo.vertices if v.nome == nome_filme), None)

    if vertice_escolhido:
        index_vertice = grafo.vertices.index(vertice_escolhido)
        conexoes = []

        for i, linha in enumerate(grafo.matriz_adjacencia):
            if linha[index_vertice] > 0:
                filme_conectado = grafo.vertices[i]
                conexoes.append(filme_conectado)

        if conexoes:
            print(f"Filmes parecidos a '{nome_filme}':")
            for filme in conexoes:
                print(f"- {filme.nome}")
        else:
            print(f"Não há filmes parecidos a '{nome_filme}'.")
    else:
        print("Filme não encontrado no grafo.")



if __name__ == "__main__":
    grafo = Grafo()
    tprint("Searchflix",font="tarty1")

    while True:
        print("\nMenu:")
        print("1.  Ler arquivo txt") 
        print("2.  Salvar em arquivo txt") 
        print("3.  Ver todos os filmes")
        print("4.  Imprimir Matriz de Adjacência")  
        print("5.  Adicionar filme") 
        print("6.  Adicionar conexao") 
        print("7.  Remover filme") 
        print("8.  Remover conexao") 
        print("9.  Consultar filmes por gênero")
        print("10. Consultar filmes por ator") 
        print("11. Procurar por filmes parecidos")
        print("12. Verificar Conectividade do grafo")
        print("13. Criar Grafo Reduzido") 

        print("0.  Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "5":
            nome = input("Nome do Filme: ")
            generos = input("Gêneros (separados por vírgula): ").split(",")
            atores = input("Atores (separados por vírgula): ").split(",")
            vertice = Vertice(nome, generos, atores)
            grafo.adicionar_vertice(vertice)
            print(f"Vértice '{nome}' adicionado ao grafo.")
        
        
        elif escolha == "6":
            nome1 = input("Nome do primeiro Filme: ")
            nome2 = input("Nome do segundo Filme: ")
            peso = int(input("Peso da aresta: "))
            vertice1 = next((v for v in grafo.vertices if v.nome == nome1), None)
            vertice2 = next((v for v in grafo.vertices if v.nome == nome2), None)
            if vertice1 and vertice2:
                grafo.adicionar_aresta(vertice1, vertice2, peso)
                print(f"Aresta entre '{nome1}' e '{nome2}' adicionada com peso {peso}.")
            else:
                print("Um ou ambos os vértices não foram encontrados.")
        elif escolha == "4":
            grafo.imprimir_matriz_adjacencia()
        elif escolha == "1":
            with open('grafo.txt', 'r') as arquivo:
              ler_filmes_e_generos(arquivo)
        elif escolha == "2":
            nome_arquivo = "salvar.txt"
            salvar_grafo_em_txt(grafo, nome_arquivo)
            print(f"Grafo salvo em '{nome_arquivo}'.")
        elif escolha == "3":
            imprimir_dados_filmes(grafo)
        elif escolha == "9":
            genero = input("Digite o gênero desejado: ")
            filmes_encontrados = grafo.consultar_filmes_por_genero(genero)
            if filmes_encontrados:
                print(f"Filmes com o gênero '{genero}':")
                for filme in filmes_encontrados:
                    print(f"- {filme.nome}")
            else:
                print(f"Nenhum filme com o gênero '{genero}' encontrado.")
        
        elif escolha == "10":
            ator = input("Digite o nome do ator desejado: ")
            filmes_encontrados = grafo.consultar_filmes_por_ator(ator)
            if filmes_encontrados:
                print(f"Filmes com o ator '{ator}':")
                for filme in filmes_encontrados:
                    print(f"- {filme.nome}")
            else:
                print(f"Nenhum filme com o ator '{ator}' encontrado.")

        elif escolha == "7":
            nome_vertice = input("Digite o nome do vértice a ser removido: ")
            vertice_a_remover = next((v for v in grafo.vertices if v.nome == nome_vertice), None)
            if vertice_a_remover:
                grafo.remover_vertice(vertice_a_remover)
            else:
                print("Vértice não encontrado.")
        elif escolha == "8":
            nome_vertice1 = input("Digite o nome do primeiro vértice: ")
            nome_vertice2 = input("Digite o nome do segundo vértice: ")
            vertice1 = next((v for v in grafo.vertices if v.nome == nome_vertice1), None)
            vertice2 = next((v for v in grafo.vertices if v.nome == nome_vertice2), None)
            if vertice1 and vertice2:
                grafo.remover_aresta(vertice1, vertice2)
            else:
                print("Um ou ambos os vértices não foram encontrados.")
        elif escolha == "12":
            conectado = grafo.verificar_conectividade()
            if conectado:
                print("O grafo é conectado.")
            else:
                print("O grafo não é conectado.")
        
        elif escolha == "13":
            grafo_reduzido = grafo.criar_grafo_reduzido()
            print("Grafo reduzido criado com sucesso.")
            grafo_reduzido.imprimir_matriz_adjacencia()
        elif escolha =="11":
          nome_filme = input("Digite o nome do filme para encontrar parecidos: ")
          filmes_conectados(grafo, nome_filme)
        elif escolha == "0":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
