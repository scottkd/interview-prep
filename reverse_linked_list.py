'''
Hooray! It's opposite day. Linked lists go the opposite way today.
Write a function for reversing a linked list . Do it in-place .

Your function will have one input: the head of the list.

Your function should return the new head of the list.

Here's a sample linked list node class:

  class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None
'''
class LinkedListNode:

	def __init__(self, value, next=None):
		self.value = value
		self.next  = next

def reverse_linked_list(head):
	if not head.next:
		return head

	next_node = head.next
	head.next = None

	stack = []
	stack.append(next_node.next)

	next_node.next = head
	curr_node = next_node

	while stack:
		next_node = stack.pop()
		if next_node.next:
			stack.append(next_node.next)
		next_node.next = curr_node
		curr_node = next_node

	return curr_node

# ----- Test Case -----
# list: c -> b -> a
# reversed should equal: a -> b -> c

a = LinkedListNode('a')
b = LinkedListNode('b', a)
c = LinkedListNode('c', b)

orig = ''
while c:
	orig += c.value
	c=c.next

a = LinkedListNode('a')
b = LinkedListNode('b', a)
c = LinkedListNode('c', b)

r = reverse_linked_list(c)

reversed_list = ''
while r:
	reversed_list += r.value
	r=r.next

assert orig[::-1] == reversed_list