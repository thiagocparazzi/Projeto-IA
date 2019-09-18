#Projeto da disciplina de Inteligência Artificial «PUC-Campinas»

def readFile():
    #lendo um arquivo txt
    file = open('letras-com-custo.txt', 'r') #abre o arquivo e lê
    #lê cada linha do arquivo 
    file_stuff = file.readlines()
    file.close()
    return file_stuff

#prepara os dados que entrarão no dicionário
def dictionary_data(data):
    d = {}
    for line in data:
        key, value, distance = line.split(',')
        key = key.replace(',', '')
        value = value.replace(',', '')
        distance = distance.replace(';', '')
        #se a chave não estiver em cidades, ele recebe um valor, caso contrário é adicionado um novo valor
        if key not in d:
            d[key] = [value, distance]
        else:
            d[key].append(value)
            d[key].append(distance)
    return d

def dictionary_data_cost(data):
    d = {}
    for line in data:
        key, value, distance = line.split(',')
        key = key.replace(',', '')
        value = value.replace(',', '')
        distance = int(distance.replace(';', '').replace('\n', ''))
        #se a chave não estiver em cidades, ele recebe um valor, caso contrário é adicionado um novo valor
        if key not in d:
            d[key] = [{value: distance}]
        else:
            d[key].append({value: distance})
            print(d[key])
    return d

#busca em largura (Breadth-First Search) entre cidade de origem e cidade de destino #FIFO
def bfs(graph, start, goal):
    #uma fila que se inicia com a cidade de origem
    queue = []
    queue.append([start])
    #enquanto a fila não estiver vazia, fará tal processo
    while queue:
        #pega o primeiro caminho (path) da fila
        path = queue.pop(0)
        #pega o último nó do caminho
        node = path[-1]
        #caso o caminho tenha sido encontrado
        if node == goal:
            return path
        #neighbours (vizinhos) recebe o grafo a partir do nó atual
        elif node in graph:
            neighbours = graph[node]
        #se um vizinho estiver no grafo de vizinhos
        #cria-se uma rota - através do caminho e adiciona tal vizinho a rota
        #a fila adiciona a rota
            for neighbour in neighbours: 
                route = list(path)
                route.append(neighbour)
                queue.append(route)

#busca em profundidade (Depth-First Search) entre cidade de origem e cidade de destino #LIFO
def dfs(graph, start, goal):
    #uma pilha que se inicia com a cidade de origem
    stack = []
    stack.append([start])
    #enquanto a pilha não estiver vazia, fará tal processo
    while stack:
        #pega o primeiro caminho (path) da pilha
        path = stack.pop()
        #pega o último nó do caminho
        node = path[-1]
        #caso o caminho tenha sido encontrado
        if node == goal:
            return path
        #neighbours (vizinhos) recebe o grafo a partir do nó atual
        elif node in graph:
            neighbours = graph[node]
        #se um vizinho estiver no grafo de vizinhos
        #cria-se uma rota - através do caminho e adiciona tal vizinho a rota
        #a pilha adiciona a rota
            for neighbour in neighbours: 
                route = list(path)
                route.append(neighbour)
                stack.append(route)

#busca de custo uniforme (Uniform Cost Search), utilizando o menor caminho entre cidades
def ucs(graph, start, goal):
    #uma fila que se inicia com a cidade de origem
    visited = []
    queue = []
    queue.append([start])
    #enquanto a fila não estiver vazia, fará tal processo
    while queue:
        #pega o primeiro caminho (path) da fila
        path = queue.pop(0)
        print('Path: ', path)
        #pega o último nó do caminho
        node = path[-1]
        if type(node) == dict:
            node = list(node.items())[0]
            print('Node -> ', node, 'Tipo - ', type(node))
            visited.append(node[0][0])
            print('Visited:', visited)
        #caso o caminho tenha sido encontrado
        if node == goal:
            return visited
        #neighbours (vizinhos) recebe o grafo a partir do nó atual
        elif node in graph:
            neighbours = graph[node]
            print('Vizinhos -> ', neighbours)
        #se um vizinho estiver no grafo de vizinhos
        #cria-se uma rota - através do caminho e adiciona tal vizinho a rota
        #a fila adiciona a rota
            for neighbour in neighbours: 
                route = list(visited)
                route.append(neighbour)
                queue.append(route)

        
#####---MAIN---#####
cities = readFile()
start = ''
goal = ''

if not cities:
    print('This file is empty')
else:
    goal = cities.pop(len(cities)-1).split()
    start = cities.pop(len(cities)-1).split()
    goal = goal[0].replace(';', '')
    start = start[0].replace(';', '')

graph = dictionary_data(cities)
graph_cost = dictionary_data_cost(cities)

bfs = bfs(graph, start, goal)
dfs = dfs(graph, start, goal)
ucs = ucs(graph_cost, start, goal)

print('Rota de Largura: ', bfs)
print('Rota de Profundidade: ', dfs)
print('Rota de Custo Uniforme: ', ucs)