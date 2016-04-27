'''
You have a singly-linked list and want to check if it contains a cycle.
A singly-linked list is built with nodes, where each node has:

node.next the next node in the list.
node.data the data held in the node. For example, if our linked list stores people in line at the movies, node.data might be the person's name.
For example:

  class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

A cycle occurs when a node's next points back to a previous node in the list. The linked list is no longer linear with a beginning and end instead, it cycles through a loop of nodes.

Write a function contains_cycle() that takes the first node in a singly-linked list and returns a boolean indicating whether the list contains a cycle.
'''
class LinkedListNode:

	def __init__(self, value, next_node=None):
		self.value = value
		self.next  = next_node

def contains_cycle(head):
	'''
	head - the head node of a singly-linked list

	returns true if the linked list contains a cycle, else false
	'''
	s = set()
	curr = head
	while curr:
		if id(curr) in s:
			return True
		s.add(id(curr))
		curr = curr.next

	return False

a = LinkedListNode('a')
b = LinkedListNode('b', a)
c = LinkedListNode('c', b)

assert contains_cycle(c) == False

d = LinkedListNode('d')
e = LinkedListNode('e')
f = LinkedListNode('f', e)
d.next = e
e.next = f

assert contains_cycle(e) == True
