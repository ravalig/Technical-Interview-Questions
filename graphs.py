class Node(object):
	def __init__(self, value):
		self.value = value
		self.edges = []

class Edge(object):
	def __init__(self, value, node_from, node_to):
		self.value = value
		self.node_from = node_from
		self.node_to = node_to

class Graph(object):
	def __init__(self, nodes=[], edges=[]):
		self.nodes = nodes
		self.edges = edges

	def insertNode(self, new_node_val):
		self.nodes.append(Node(new_node_val))

	def insertEdge(self, new_edge_val, node_from_val, node_to_val):
		from_found = None 
		to_found = None

		for node in self.nodes:
			if node.value == node_from_val:
				from_found = node_from
			if node.value == node_to_val:
				to_found == node_to

		if from_found == None:
			from_found = Node(node_from_val)
			self.nodes.append(from_found)

		if to_found == None:
			to_found = Node(node_to_val)
			self.nodes.append(to_found)

		new_edge = Edge(new_edge_val, from_found, to_found)
		from_found.edges.append(new_edge)
		to_found.edges.append(new_edge)
		self.edges.append(new_edge)

	def get_edge_list(self):
		"""Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
		results =[]
		for edge in self.edges:
			results.append((edge.value, edge.node_from.value, edge.node_to.value))
		return results


		

