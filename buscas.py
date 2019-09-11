#criando lista para adicionar as cidades do arquivo
cities = {} #poderia ser também cities = file.readLines()

def readFile():
    #lendo um arquivo txt
    file = open('cidades.txt', 'r') #abre o arquivo e lê
    #lê cada linha do arquivo 
    for line in file:
        key, value = line.split()
        key = key.replace(',', '')
        
        if key not in cities:  #se a chave não estiver em cidades, ele recebe um valor, caso contrário é adicionado um novo valor
            cities[key] = [value]
        else:
            cities[key].append(value)

    file.close()

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
        #se um vizinho estvier no grafo de vizinhos
        #cria-se uma rota - através do caminho e adiciona tal vizinho a rota
        #a fila adiciona a rota
        for neighbour in neighbours:
            route = list(path)
            route.append(neighbour)
            queue.append(route)
 
readFile()
#bfs(nome_do_grafo, cidade_origem, cidade_destino)
print(bfs(cities, 'SBO', 'Campinas'))
