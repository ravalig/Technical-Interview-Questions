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


import pprint
pp = pprint.PrettyPrinter(indent=2)

class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes or []
        self.edges = edges or []
        self.node_names = []
        self._node_map = {}

    def set_node_names(self, names):
        """The Nth name in names should correspond to node number N.
        Node numbers are 0 based (starting at 0).
        """
        self.node_names = list(names)

    def insert_node(self, new_node_val):
        "Insert a new node with value new_node_val"
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        self._node_map[new_node_val] = new_node
        return new_node

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        "Insert a new edge, creating new nodes if necessary"
        nodes = {node_from_val: None, node_to_val: None}
        for node in self.nodes:
            if node.value in nodes:
                nodes[node.value] = node
                if all(nodes.values()):
                    break
        for node_val in nodes:
            nodes[node_val] = nodes[node_val] or self.insert_node(node_val)
        node_from = nodes[node_from_val]
        node_to = nodes[node_to_val]
        new_edge = Edge(new_edge_val, node_from, node_to)
        node_from.edges.append(new_edge)
        node_to.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_adjacency_list(self):
        """Return a list of lists.
        The indecies of the outer list represent "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""
        max_index = self.find_max_index()
        adjacency_list = [[] for _ in range(max_index)]
        for edg in self.edges:
            from_value, to_value = edg.node_from.value, edg.node_to.value
            adjacency_list[from_value].append((to_value, edg.value))
        return [a or None for a in adjacency_list] # replace []'s with None


    def get_adjacency_list_names(self):
        
        adjacency_list = self.get_adjacency_list()

        def convert_to_names(pair, graph=self):
            node_number, value = pair
            return (graph.node_names[node_number], value)

        def map_conversion(adjacency_list_for_node):
            if adjacency_list_for_node is None:
                return None
            return map(convert_to_names, adjacency_list_for_node)

        return [map_conversion(adjacency_list_for_node)
                for adjacency_list_for_node in adjacency_list]

    def find_max_index(self):
        """Return the highest found node number
        Or the length of the node names if set with set_node_names()."""
        if len(self.node_names) > 0:
            return len(self.node_names)
        max_index = -1
        if len(self.nodes):
            for node in self.nodes:
                if node.value > max_index:
                    max_index = node.value
        return max_index

def find_minVertex(keys, vertices, mstSet):
    temp = []
    for i in keys:
        temp.append(i)
    for mst_vertex in mstSet:
        vertex_index = vertices.index(mst_vertex)
        temp[vertex_index] = float("inf")
    return temp.index(min(temp))

def getInputKeys(vertices_input):
	vertices_input_keys = []
	sd = sorted(vertices_input.items())
	for k,v in sd:
		vertices_input_keys.append(k)
	return vertices_input_keys

def getInputValues(vertices_input):
    vertices_input_values = []
    sd = sorted(vertices_input.items())
    for k,v in sd:
    	vertices_input_values.append(v)
    return vertices_input_values

def question3(vertices_input):
	if vertices_input != None:

		if None in vertices_input.keys():
			error = "Invalid Input"
			return error

		vertices_input_keys = getInputKeys(vertices_input)
		vertices_input_values = getInputValues(vertices_input)

		str_to_int = {}
		counter = 0
		for key in vertices_input_keys:
			str_to_int[key] = counter
			counter +=1

		temp = []
		for i in vertices_input_values:
			temp_j = []
			for j in i:
				j = (str_to_int[j[0]],j[1])
				temp_j.append(j)
			temp.append(temp_j)


		vertices_input = dict(zip(sorted(str_to_int.values()),temp))
    
		vertices = list(vertices_input.keys())   # set of vertices

		keys = []      # list of keys used to pick minimum weight edge
		keys.append(0)

		mstSet= []      # Holds vertices not yet included in finalMST
    
		mstGraph = Graph()
		for i in range(1,len(vertices)):
			keys.append(float("inf"))

		minVal = -1
		while(len(vertices) > len(mstSet)):
			if(minVal == -1):
				previous_vertex = vertices[0]
				vertex = vertices[0]
				mstSet.append(vertex)
				adjacent_vertices = vertices_input[vertex]
				for adjacent_vertex in adjacent_vertices:
					vertex_index = vertices.index(adjacent_vertex[0])
					keys[vertex_index] = adjacent_vertex[1]
				minVal = 0
			else:
				vertex = find_minVertex(keys,vertices, mstSet)
				mstSet.append(vertex)

				mstGraph.insert_edge(keys[vertices.index(vertex)], previous_vertex, vertex)
				mstGraph.insert_edge(keys[vertices.index(vertex)], vertex, previous_vertex)
				previous_vertex = vertex

				adjacent_vertices = vertices_input[vertex]
				for adjacent_vertex in adjacent_vertices:
					vertex_index = vertices.index(adjacent_vertex[0])
					if(adjacent_vertex[1] < keys[vertex_index]):
						keys[vertex_index] = adjacent_vertex[1]

		mstGraph.set_node_names((i for i in sorted(str_to_int)))

		results_dict = {}
		temp = mstGraph.get_adjacency_list()
		for i in range(0,len(temp)):
			results_dict[i] = temp[i]

		names = mstGraph.get_adjacency_list_names()
		x_list = []
		for x in names:
			y_list =[]
			for y in x:
				y_list.append(y) 
			x_list.append(y_list)

		names_dict = dict(zip(sorted(str_to_int), x_list))

		return names_dict

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

    def search(self, find_val):
    	self.search_path = []
    	return self.search_helper(self.root, find_val)

    def search_helper(self, current, find_val):
        if current:
            if current.value == find_val:
            	self.search_path.append(current.value)
            	return True
            elif current.value < find_val:
            	self.search_path.append(current.value)
            	return self.search_helper(current.right, find_val)
            else:
            	self.search_path.append(current.value)
            	return self.search_helper(current.left, find_val)
        return False

def question4(T, r, n1, n2):
	if(T == None or n1 >= len(T) or n2 >= len(T)):
		error = "Invalid input"
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

	if(tree.search(n1)):
		n1_path = tree.search_path

	if(tree.search(n2)):
		n2_path = tree.search_path

	min_ancestor = None
	for i in range(0,min(len(n1_path), len(n2_path))):
		if n1_path[i] == n2_path[i]:
			min_ancestor = n1_path[i]
		else:
			return min_ancestor
	return min_ancestor


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