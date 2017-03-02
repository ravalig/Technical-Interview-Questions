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

	print(n1_path)
	print(n2_path)

	min_ancestor = None
	for i in range(0,min(len(n1_path), len(n2_path))):
		if n1_path[i] == n2_path[i]:
			min_ancestor = n1_path[i]
		else:
			return min_ancestor
	return min_ancestor


T = [[0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [1, 0, 0, 0, 1],
     [0, 0, 0, 0, 0]]

print(question4(T, 3, 0, 1))