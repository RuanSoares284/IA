import numpy as np


#Class Vertice e class Adjacente
class Vertice:
    def __init__(self, rotulo, distancia_objetivo):
        self.rotulo = rotulo  #nome
        self.visitado = False  #se o vertice foi visitado
        self.distancia_objetivo = distancia_objetivo  #a distância do vértice do objetivo
        self.adjacentes = []  #vertices vizinhos a este vertice

    def adiciona_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)

    def mostra_adjacentes(self):
        for i in self.adjacentes:
            print(i.vertice.rotulo, i.custo)


class Adjacente:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo
        self.distancia_aestrela = vertice.distancia_objetivo + self.custo


#class Grafo e main
class Grafo:
    #Distância em linha reta das cidades até Bucareste
    arad = Vertice('Arad', 366)
    bucareste = Vertice('Bucareste', 0)
    craiova = Vertice('Craiova', 160)
    drobeta = Vertice('Drobeta', 242)
    eforie = Vertice('Eforie', 161)
    fagaras = Vertice('Fagaras', 176)
    giurgiu = Vertice('Giurgiu', 77)
    hirsova = Vertice('Hirsova', 151)
    iasi = Vertice('Iasi', 226)
    lugoj = Vertice('Lugoj', 244)
    mehadia = Vertice('Mehadia', 241)
    neamt = Vertice('Neamt', 234)
    oradea = Vertice('Oradea', 380)
    pitesti = Vertice('Pitesti', 100)
    rimnicu_vilcea = Vertice('Rimnicu Vilcea', 193)
    sibiu = Vertice('Sibiu', 253)
    timisoara = Vertice('Timisoara', 329)
    urziceni = Vertice('Urziceni', 80)
    vaslui = Vertice('Vaslui', 199)
    zerind = Vertice('Zerind', 374)

    #Distância de Arad com as cidades adjacentes
    arad.adiciona_adjacente(Adjacente(zerind, 75))
    arad.adiciona_adjacente(Adjacente(timisoara, 118))
    arad.adiciona_adjacente(Adjacente(sibiu, 140))

    #Distância de Bucareste com as cidades adjacentes
    bucareste.adiciona_adjacente(Adjacente(pitesti, 101))
    bucareste.adiciona_adjacente(Adjacente(giurgiu, 90))
    bucareste.adiciona_adjacente(Adjacente(urziceni, 85))

    #Distância de Craiova com as cidades adjacentes
    craiova.adiciona_adjacente(Adjacente(drobeta, 120))
    craiova.adiciona_adjacente(Adjacente(pitesti, 138))
    craiova.adiciona_adjacente(Adjacente(rimnicu_vilcea, 146))

    #Distância de Drobeta com as cidades adjacentes
    drobeta.adiciona_adjacente(Adjacente(mehadia, 75))
    drobeta.adiciona_adjacente(Adjacente(craiova, 120))

    #Distância de Eforie com as cidades adjacentes
    eforie.adiciona_adjacente(Adjacente(hirsova, 86))

    #Distância de Fagaras com as cidades adjacentes
    fagaras.adiciona_adjacente(Adjacente(sibiu, 99))
    fagaras.adiciona_adjacente(Adjacente(bucareste, 211))

    #Distância de Giurgiu com as cidades adjacentes
    giurgiu.adiciona_adjacente(Adjacente(bucareste, 90))

    #Distância de Hirsova com as cidades adjacentes
    hirsova.adiciona_adjacente(Adjacente(eforie, 86))
    hirsova.adiciona_adjacente(Adjacente(urziceni, 98))

    #Distância de Iasi com as cidades adjacentes
    iasi.adiciona_adjacente(Adjacente(neamt, 87))
    iasi.adiciona_adjacente(Adjacente(vaslui, 92))

    #Distância de Lugoj com as cidades adjacentes
    lugoj.adiciona_adjacente(Adjacente(timisoara, 111))
    lugoj.adiciona_adjacente(Adjacente(mehadia, 70))

    #Distância de Mehadia com as cidades adjacentes
    mehadia.adiciona_adjacente(Adjacente(lugoj, 70))
    mehadia.adiciona_adjacente(Adjacente(drobeta, 75))

    #Distância de Neamt com as cidades adjacentes
    neamt.adiciona_adjacente(Adjacente(iasi, 87))

    #Distância de Oradea com as cidades adjacentes
    oradea.adiciona_adjacente(Adjacente(zerind, 71))
    oradea.adiciona_adjacente(Adjacente(sibiu, 151))

    #Distância de Pitesti com as cidades adjacentes
    pitesti.adiciona_adjacente(Adjacente(rimnicu_vilcea, 97))
    pitesti.adiciona_adjacente(Adjacente(craiova, 138))
    pitesti.adiciona_adjacente(Adjacente(bucareste, 101))

    #Distância de Rimnicu Vilcea com as cidades adjacentes
    rimnicu_vilcea.adiciona_adjacente(Adjacente(pitesti, 97))
    rimnicu_vilcea.adiciona_adjacente(Adjacente(craiova, 146))
    rimnicu_vilcea.adiciona_adjacente(Adjacente(sibiu, 80))

    #Distância de Sibiu com as cidades adjacentes
    sibiu.adiciona_adjacente(Adjacente(arad, 140))
    sibiu.adiciona_adjacente(Adjacente(oradea, 151))
    sibiu.adiciona_adjacente(Adjacente(rimnicu_vilcea, 80))
    sibiu.adiciona_adjacente(Adjacente(fagaras, 99))

    #Distância de Timisoara com as cidades adjacentes
    timisoara.adiciona_adjacente(Adjacente(arad, 118))
    timisoara.adiciona_adjacente(Adjacente(lugoj, 111))

    #Distância de Urziceni com as cidades adjacentes
    urziceni.adiciona_adjacente(Adjacente(bucareste, 85))
    urziceni.adiciona_adjacente(Adjacente(hirsova, 98))
    urziceni.adiciona_adjacente(Adjacente(vaslui, 142))

    #Distância de Vaslui com as cidades adjacentes
    vaslui.adiciona_adjacente(Adjacente(iasi, 92))
    vaslui.adiciona_adjacente(Adjacente(urziceni, 142))

    #Distância de Zerind com as cidades adjacentes
    zerind.adiciona_adjacente(Adjacente(oradea, 71))
    zerind.adiciona_adjacente(Adjacente(arad, 75))


#Criando o Grafo
grafo = Grafo()


#Class VetorOrdenado
class VetorOrdenado:  #armazena as cidades adjacentes
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=object)

    # Referência para o vértice e comparação com a distancia A*
    def insere(self, adjacente):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return
        posicao = 0
        for i in range(self.ultima_posicao + 1):  # percorre todo o vetor
            posicao = i
            if self.valores[
                    i].distancia_aestrela > adjacente.distancia_aestrela:
                break
            if i == self.ultima_posicao:  #caso para atualizar última posicao
                posicao = i + 1
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x +
                         1] = self.valores[x]  # desloca valores para inserção
            x -= 1
        self.valores[posicao] = adjacente
        self.ultima_posicao += 1

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(self.valores[i].vertice.rotulo, ': ',
                      self.valores[i].custo, ' + ',
                      self.valores[i].vertice.distancia_objetivo, ' = ',
                      self.valores[i].distancia_aestrela)


#Class A Estrela (A*)
class AEstrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo  # --- self.parametro -->atributo
        self.encontrado = False

    def buscar(self, atual):  # função de teste de objetivo
        print('-------------------------------------------------------')
        print('Nó Atual: {}'.format(atual.rotulo))
        atual.visitado = True  # marca o atual como visitanto

        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = VetorOrdenado(
                len(atual.adjacentes
                    ))  #criar um vetor ordenado com tamanho da quantidade
            for adjacente in atual.adjacentes:  # percorre a lista de vizinhos do grafo atual
                if adjacente.vertice.visitado == False:  # se o vizinho ainda não foi visitado
                    adjacente.vertice.visitado = True  #marcar como visitado
                    vetor_ordenado.insere(
                        adjacente
                    )  #inserir dentro do vetor ordenado como um vizinho do nó atual
            vetor_ordenado.imprime()  #mostra os vizinhos so nó atual

            if vetor_ordenado.valores[
                    0] != None:  # se o vetor ordenado tiver algum objeto no início
                self.buscar(
                    vetor_ordenado.valores[0].vertice
                )  # busca pelo inicío do vetor ordenado (como é ordenado)


#Menu
aux = False

print('''------------------ CIDADES DE ORIGEM ------------------
1.Arad 
2.Bucareste
3.Craiova
4.Drobeta
5.Eforie
6.Fagaras
7.Giurgiu
8.Hirsova
9.Iasi
10.Lugoj
11.Mehadia
12.Neamt
13.Oradea
14.Pitesti
15.Rimnicu Vilcea
16.Sibiu
17.Timisoara
18.Urziceni
19.Vaslui
20.Zerind
-------------------------------------------------------''')
while (aux == False):
    opção = int(input("Escolha a cidade de Origem com Destino a Bucareste: "))

    if opção == 1:
        busca_aestrela = AEstrela(grafo.bucareste)
        busca_aestrela.buscar(grafo.arad)
        aux = True

    elif opção == 2:
        busca_aestrela = AEstrela(grafo.bucareste)
        busca_aestrela.buscar(grafo.bucareste)
        aux = True

    elif opção == 3:
        busca_aestrela = AEstrela(grafo.bucareste)
        busca_aestrela.buscar(grafo.craiova)
        aux = True

    elif opção == 4:
        busca_aestrela = AEstrela(grafo.bucareste)
        busca_aestrela.buscar(grafo.drobeta)
        aux = True

    elif opção == 5:
        busca_aestrela = AEstrela(grafo.bucareste)
        busca_aestrela.buscar(grafo.eforie)
        aux = True

    elif opção == 6:
        busca_aestrela = AEstrela(grafo.bucareste)
        busca_aestrela.buscar(grafo.fagaras)
        aux = True

    elif opção == 7:
        busca_aestrela = AEstrela(grafo.bucareste)
        busca_aestrela.buscar(grafo.giurgiu)
        aux = True

    elif opção == 8:
        busca_aestrela = AEstrela(grafo.bucareste)
        busca_aestrela.buscar(grafo.hirsova)
        aux = True

    elif opção == 9:
        busca_aestrela = AEstrela(grafo.bucareste)
        busca_aestrela.buscar(grafo.iasi)
        aux = True

    elif opção == 10:
        busca_aestrela = AEstrela(grafo.bucareste)
        busca_aestrela.buscar(grafo.lugoj)
        aux = True

    elif opção == 11:
        busca_aestrela = AEstrela(grafo.bucareste)
        busca_aestrela.buscar(grafo.mehadia)
        aux = True

    elif opção == 12:
        busca_aestrela = AEstrela(grafo.bucareste)
        busca_aestrela.buscar(grafo.neamt)
        aux = True

    elif opção == 13:
        busca_aestrela = AEstrela(grafo.bucareste)
        busca_aestrela.buscar(grafo.oradea)
        aux = True

    elif opção == 14:
        busca_aestrela = AEstrela(grafo.bucareste)
        busca_aestrela.buscar(grafo.pitesti)
        aux = True

    elif opção == 15:
        busca_aestrela = AEstrela(grafo.bucareste)
        busca_aestrela.buscar(grafo.rimnicu_vilcea)
        aux = True

    elif opção == 16:
        busca_aestrela = AEstrela(grafo.bucareste)
        busca_aestrela.buscar(grafo.sibiu)
        aux = True

    elif opção == 17:
        busca_aestrela = AEstrela(grafo.bucareste)
        busca_aestrela.buscar(grafo.timisoara)
        aux = True

    elif opção == 18:
        busca_aestrela = AEstrela(grafo.bucareste)
        busca_aestrela.buscar(grafo.urziceni)
        aux = True

    elif opção == 19:
        busca_aestrela = AEstrela(grafo.bucareste)
        busca_aestrela.buscar(grafo.vaslui)
        aux = True

    elif opção == 20:
        busca_aestrela = AEstrela(grafo.bucareste)
        busca_aestrela.buscar(grafo.zerind)
        aux = True

    else:
        print("Opção incorreta!")
        aux = False
