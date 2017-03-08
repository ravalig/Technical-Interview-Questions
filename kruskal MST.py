parent = dict()
rank = dict()

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1

def tranformGraph(G):
    '''
        Transforms the graph G which is represented as Adjacency list into a
        dictionary of vertices and edges
    '''
    vertices = list(G.keys())
    vertices.sort()

    edges = []

    for k,v in G.items():
        node1 = k
        for vv in v:
            weight = vv[1]
            node2 = vv[0]
            temp = [weight, node1, node2]
            if(len(edges) != 0):
                duplicate=False
                for e in edges:
                    eList = [e[0], e[1], e[2]]
                    if(temp[0] in eList and temp[1] in eList and temp[2] in eList):
                        duplicate = True
                if(duplicate == False):
                    edges.append((weight, node1, node2))
            else:
                edges.append((weight, node1, node2))

    graph = {'vertices': vertices,
             'edges': set(edges)
            }

    return graph


def getAdjacencyList(mst):
    '''
        This function returns a minimum spanning tree in adjacency list format
    '''
    mstAL= {}

    for i in mst:
        for x in range(1,3):
            if(x == 1):
                y = 2
            elif(x == 2):
                y = 1 

            if(i[x] in mstAL.keys()):
                mstAL[i[x]].append((i[y], i[0]))
            else:
                mstAL[i[x]] = []
                mstAL[i[x]].append((i[y], i[0]))
    return mstAL


def kruskal(inputGraph):
    if(inputGraph != None):
        if None in inputGraph.keys():
            error = "Invalid Input"
            return error

        graph = tranformGraph(inputGraph)
        for vertice in graph['vertices']:
            make_set(vertice)

        minimum_spanning_tree = set()
        edges = list(graph['edges'])
        edges.sort()
        for edge in edges:
            weight, vertice1, vertice2 = edge
            if find(vertice1) != find(vertice2):
                union(vertice1, vertice2)
                minimum_spanning_tree.add(edge)
        mstAL = getAdjacencyList(minimum_spanning_tree)
        return mstAL
    else:
        error = "Invalid Input"
        return error


G = {
     'A':[('B',2)], 
     'B':[('A',2),('C',5), ('D',3)],
     'C':[('B',5),('D',2)],
     'D':[('B',3),('C',2)]
    }
print(kruskal(G))