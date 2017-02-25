class Node(object):
  def __init__(self, data=None):
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
	current = ll
	counter = 1
	temp = ll

	while(current):
		if(counter > m):			
			temp = temp.next
			
		current = current.next
		counter += 1
	return temp


llist = LinkedList(Node(10))
llist.append(Node(11))
llist.append(Node(12))
llist.append(Node(13))
llist.append(Node(14))

result = question5(llist.head, 5)
print(result.data)
