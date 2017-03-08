def question1(source,target):
	source_len = len(source)
	target_len = len(target)
	source = source.lower()
	target = target.lower()

	if(target_len > source_len):
		return False
	else:
		source_dict = {}
		target_dict = {}

		for j in target:
			if(j not in target_dict):
				target_dict[j] = 1
			else:
				target_dict[j] += 1

		start = 0
		end = target_len

		while(end <= source_len):
			temp = source[start:end]
			temp_dict = {}
			for i in temp:
				if(i not in temp_dict):
					temp_dict[i] = 1
				else:
					temp_dict[i] += 1
			if(temp_dict == target_dict):
				return True
			else:
				start +=1
				end += 1
		return False

# --------------------------------------------------------------------------
def question2(test):
	length = len(test)
	pal_Length = 1
 
	start = 0 
	low = 0
	high = 0
	for i in range(1, length):
    	# Even
		low = i - 1
		high = i
		while low >= 0 and high < length and test[low] == test[high]:
			if high - low + 1 > pal_Length:
				start = low
				pal_Length=high-low + 1
			low -= 1
			high += 1
 
        # Odd
		low = i-1
		high = i+1
		while low>=0 and high<length and test[low]==test[high]:
			if high - low + 1 > pal_Length:
				start=low
				pal_Length = high-low + 1
			low -= 1
			high += 1
 
	result = test[start:start + pal_Length]
	return result
# --------------------------------------------------------------------------

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


def question3(inputGraph):
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

# --------------------------------------------------------------------------

from collections import deque

class Node_BST(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node_BST(root)
        self.search_path = []

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Node_BST(new_val)
        else:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node_BST(new_val)

def LCAHelper(root, n1, n2):
	if(root == None):
		error = "Invalid Input"
		return None

	if root.value == n1 or root.value == n2:
		return root

	left_lca = LCAHelper(root.left, n1, n2) 
	right_lca = LCAHelper(root.right, n1, n2)

	if left_lca and right_lca:
		return root 

	return left_lca if left_lca is not None else right_lca

def question4(T, r, n1, n2):
	if(T == None or n1 >= len(T) or n2 >= len(T)):
		error = "Invalid Input"
		return error

	NotTraversed = deque([r])
	while(NotTraversed):
		pos = NotTraversed.popleft()
		for i in range(0,len(T[pos])):
			if T[pos][i] == 1:
				NotTraversed.append(i)
		if pos == r:
			tree = BST(r)
		else:
			tree.insert(pos)

	temp = LCAHelper(tree.root, n1, n2)
	if temp:
		return temp.value


# --------------------------------------------------------------------------

class Element(object):
	def __init__(self,data=None):
		self.data = data
		self.next = None
class LinkedList(object):
	def __init__(self, new_element):
		self.head = new_element

	def append(self, new_element):
		current = self.head
		if(self.head):
			while current.next:
				current = current.next
			current.next = new_element
		else:
			self.head = new_element

def question5(ll, m):
	if(ll == None or m == None or m <= 0):
		print("Invalid  Input")
		return None
	else:

		current = ll
		counter = 1
		temp = ll

		while(current):
			if(counter > m):			
				temp = temp.next
			
			current = current.next
			counter += 1
		return temp

# --------------------------------------------------------------------------

print("---------QUESTION 1---------")


print(question1("udacity", "Da"))
# Expected output : True
print(question1("udacity", "ra"))
# Expected output : False
print(question1("udacity", "udacity"))
# Expected output : True

print("---------QUESTION 2---------")

print(question2("nitin"))
# Expected output : nitin
print(question2("venu"))
# Expected output : v
print(question2("12345"))
# Expected output : 1

print("---------QUESTION 3---------")


G = {'A':[('B',2)], 
          'B':[('A',2),('C',5), ('D',3)],
          'C':[('B',5),('D',2)],
          'D':[('B',3),('C',2)]
         }

G1 = {'A':[('B',2)], 
          'B':[('A',2),('C',5), ('D',3)],
          None:[('B',5),('D',2)],
          'D':[('B',3),('C',2)]
         }
print(question3(G))
# Expected output : {'A': [('B', 2)], 'D': [('B', 3), ('C', 2)], 'C': [('D', 2)], 'B': [('A', 2), ('D', 3)]}
print(question3(G1))
# Expected output : Invalid Input
print(question3(None))
# Expected output : Invalid Input


print("---------QUESTION 4---------")


T = [[0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [1, 0, 0, 0, 1],
     [0, 0, 0, 0, 0]]

print(question4(T, 3, 0, 1))
# Expected output :  0
print(question4(None, 3, 0, 1))
# Expected output :  Invalid Input
print(question4(T, 3, 5, 1))
# Expected output :  Invalid Input

print("---------QUESTION 5---------")

llist = LinkedList(Element(10))
llist.append(Element(11))
llist.append(Element(12))
llist.append(Element(13))
llist.append(Element(14))

if question5(llist.head, 5):
	print(question5(llist.head, 5).data)
	# Expected output :  10
if question5(llist.head, -1):
	print(question5(llist.head, -1).data)
	# Expected output : Invalid Input
if question5(llist.head, None):
	print(question5(llist.head, None).data)
	# Expected output :  Invalid Input