'''
You have a linked list and want to find the kth to last node.
Write a function kth_to_last_node() that takes an integer k and the head_node of a singly linked list, and returns the kth to last node in the list.
'''
class LinkedListNode:
	def __init__(self, value):
		self.value = value
		self.next  = None

def kth_to_last_node(k, head):
	curr = head
	node_list = []
	while curr:
		node_list.append(curr)
		curr = curr.next	

	if len(node_list) < k:
		raise IndexError('Invalid index')

	return node_list[len(node_list) - k]


# ----- Test Case -----
a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

assert kth_to_last_node(2, a).value == "Devil's Food"
# returns the node with value "Devil's Food" (the 2nd to last node)
