import LinkedList as ll

'''
Question 24
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without
modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Ideas
- We can start at the beginning of the LL and go by increments of 2 to see if we should swap
	- With each group of 2, need to check if there is a next element (also need to ensure that we don't modify the values in the list nodes)
	- Instead should swap each potential pair

'''

# Testing these functions

l1 = ll.ListNode(1, ll.ListNode(2, ll.ListNode(3)))
l2 = ll.ListNode(4)
l3 = ll.listToLink([1, 2, 3, 4, 5])
l4 = ll.listToLink([1, 2, 3, 4, 5, 6])

l01 = ll.ListNode(1, ll.ListNode(2, ll.ListNode(3)))
l02 = ll.ListNode(4)
l03 = ll.listToLink([1, 2, 3, 4, 5])
l04 = ll.listToLink([1, 2, 3, 4, 5, 6])


# print(getStringLL(l1))
# print(getStringRecursiveLL(l1))
# print(getStringLL(l2))
# print(getStringRecursiveLL(l2))
# print(getStringLL(l3))
# print(getStringRecursiveLL(l3))
# print(getStringLL(l4))
# print(getStringRecursiveLL(l4))

# Recursive Version
def swapNodes(head):
	def helper(head):
		if head is None or head.next is None:
			return head
		else:
			curr = head
			n = curr.next
			nn = curr.next.next
			n.next = curr
			curr.next = nn
			head.next = helper(nn)
			return n
	return helper(head)

# Iterative Version--using many, many pointers
def swapNodes2(head):
	if head is None or head.next is None: # If we are working with a 0 or 1 element LL
		return head # Can directly return (since there's no swapping needed)
	else:
		prev = anchor = ll.ListNode(-1, head) # Provide an anchor + the previous value allowing for manipulation of the main linked list
		curr = temp = head # Curr points to the current element of the LL, temp follows suit
		while temp:
			curr = temp # Move the value of the current to reflect the subset of the LL values we want to change
			n = curr.next # Existing immediate successor to current element
			if not n: # If we don't have a successor --> no need to manipulate further (meaning working with a single element LL)
				break # Terminate the looping
			prev.next = n # Previous value should be pointing to current's successor
			temp = n.next # Want temp to be the reference for the successor's successor for next iteration
			n.next = curr # Want the current successor to current element to point backward towards current
			curr.next = temp # Successor to the current element should be current successor's successor
			prev = curr # Move previous to the "previous" element in the next iteration
		return anchor.next # Anchor referred to original extra "node" linked list, so we want the next element
			

def testSwapNodes():
	print(ll.printListNode(swapNodes(l1))) # 2 -> 1 -> 3
	print(ll.printListNode(swapNodes(l2))) # 4
	print(ll.printListNode(swapNodes(l3))) # 2 -> 1 -> 4 -> 3 -> 5
	print(ll.printListNode(swapNodes(l4))) # 2 -> 1 -> 4 -> 3 -> 6 -> 5

	print(ll.printListNode(swapNodes2(l01))) # 2 -> 1 -> 3
	print(ll.printListNode(swapNodes2(l02))) # 4
	print(ll.printListNode(swapNodes2(l03))) # 2 -> 1 -> 4 -> 3 -> 5
	print(ll.printListNode(swapNodes2(l04))) # 2 -> 1 -> 4 -> 3 -> 6 -> 5

testSwapNodes()
