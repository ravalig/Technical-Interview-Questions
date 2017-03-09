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
	if(T == None):
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



T = [[0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0],
     [1, 0, 0, 0, 1],
     [0, 0, 0, 0, 0]]

print(question4(T, 3, 0, 4))