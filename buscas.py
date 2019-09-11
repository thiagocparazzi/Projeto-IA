def readFile():
    #lendo um arquivo txt
    file = open('cidades.txt', 'r') #abre o arquivo e lê
    #lê cada linha do arquivo 
    file_stuff = file.readlines()
    file.close()
    return file_stuff

#prepara os dados que entrarão no dicionário
def dictionary_data(data):
    d = {}
    for n in range(0, len(data)):
        key, value = data[n].split()
        key = key.replace(',', '')
        value = value.replace(';', '')
        #se a chave não estiver em cidades, ele recebe um valor, caso contrário é adicionado um novo valor
        if key not in d:
            d[key] = [value]
        else:
            d[key].append(value)
    return d

#busca em largura (Breadth-First Search) entre cidade de origem e cidade de destino
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
        neighbours = graph[node]
        #se um vizinho estiver no grafo de vizinhos
        #cria-se uma rota - através do caminho e adiciona tal vizinho a rota
        #a fila adiciona a rota
        for neighbour in neighbours:
            route = list(path)
            route.append(neighbour)
            queue.append(route)

#busca em largura (Depth-First Search) entre cidade de origem e cidade de destino
def dfs(graph, start, goal):
    #a pilha inicia-se com a cidade de origem
    stack = [(start, [start])]
    #prepara a lista de nós visitados
    visited = set()
    #enquanto a pilha não estiver vazia, fará tal processo
    while stack:
        #node e path recebem o último valor da pilha
        (node, path) = stack.pop()
        #se o nó não estiver em visitado, será adicionado
        if node not in visited:
            if node == goal:
                return path
            visited.add(node)
            #neighbours (vizinhos) recebe o grafo a partir do nó atual
            neighbours = graph[node]
            #os vizinhos do grafo atual serão adicionados a fila, junto com seu caminho e lista de vizinhos
            for neighbour in neighbours:
                stack.append((neighbour, path + [neighbour]))
        
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
bfs = bfs(graph, start, goal)
dfs = dfs(graph, start, goal)
#bfs(nome_do_grafo, cidade_origem, cidade_destino)
print('Rota de Largura: ', bfs)
print('Rota de Profundidade: ', dfs)
