class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iterative version of printing out a linked list
def printListNode(node):
	ll_printed = ''
	while node != None:
		ll_printed += str(node.val) + ' -> '
		node = node.next
	return ll_printed[:-3]

# Recursive version of printing out the linked list
def printRecursiveLL(node):
	if node == None:
		return
	elif node.next == None:
		return str(node.val)
	else:
		return str(node.val) + ' -> ' + printRecursiveLL(node.next)


# Construct a linked list from a Python list
def listToLink(list_values):
	if len(list_values) == 0: # Base case 1: list is empty
		return None
	elif len(list_values) == 1: # Base case 2: list of length 1
		return ListNode(list_values[0])
	else:
		return ListNode(list_values[0], listToLink(list_values[1:]))
