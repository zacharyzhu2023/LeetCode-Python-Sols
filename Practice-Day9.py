# Reverse a Linked List

import LinkedList as ll
def reverseLL(lst):
	if lst is None or lst.next is None: # Base case when we're working with a null or 1 element LL
		return lst # Can directly return
	else:
		#print('ll:', ll.printListNode(lst))
		curr = lst # Pointers to the beginning of the LL
		prev = None
		while curr:
			nxt = curr.next # Get the next linked list (excluding present element)
			curr.next = prev # THe next element of the current element should be all the previously accumulated reversed LL
			prev = curr # Increment prev pointer
			curr = nxt # Increment curr pointer based off of previously saved next LL
		#print('ll:', ll.printListNode(lst))
		return prev

# Get the length of the linked list
def lengthLL(ll):
	p = head # Get a generic pointer to the head of the LL
	length = 0 # Track how many "next's" we have reached
	while head is not None:
		p = p.next
		length += 1
	return length

'''
Question 25
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number 
of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

'''

'''
- Intuition: use a while loop to reverse the LL by groups of k
	- Change the pointer: within that group, the starting pointer + ending pointer get flipped
- After each group flip, check to see if we have sufficient elements to flip--if so, move the pointer
	- Otherwise, return the head
'''
def reverseKGroup(head, k):
	# Need to determine the length of the original linked list
	length = 0
	p = head
	while p is not None:
		p = p.next
		length += 1
	curr = head # Pointer to the head of the LL
	dummy = prev = ll.ListNode(0, curr) # Dummy variable that incorporates the current value of the 
	#print(ll.printListNode(dummy))
	while length >= k:
		# Reverse the current linked list (k elements at hand)
		for i in range(k-1):
			nxt = curr.next # Get the next element in the linked list
			curr.next = nxt.next # Move what the current element's successor is
			nxt.next = prev.next # Reverse LL (for a given link)
			prev.next = nxt # Change previous pointer increment
		length -= k # Decrement the count of number of nodes
		prev = curr # Change the pointer to start reversing a new iteration
		if prev.next:
			curr = prev.next # Curr is pointing to a new LL to reverse
		if curr.next:
			nxt = curr.next # Next element after curr
		# Change the pointers (in terms of the current and next element)
	return dummy.next # Since we had a pseudo-first node

def reverseKGroup2(head, k):
	def reverseTemp(lst, k): # Return the previous and new head pointer
		start = curr = lst # Pointers to the beginning of the LL
		prev = None
		count = k
		while count > 0 and curr:
			nxt = curr.next # Get the next linked list (excluding present element)
			curr.next = prev # THe next element of the current element should be all the previously accumulated reversed LL
			prev = curr # Increment prev pointer
			curr = nxt # Increment curr pointer based off of previously saved next LL
			length -= 1
		#print('ll:', ll.printListNode(lst))
		return curr, start, length
	newStart = head
	prev = None
	isFirst = True
	while True:
		if isFirst:
			tempStart, tempEnd, count = reverseTemp(newHead, k)
			if count == 0:
				prev.next = tempStart
				prev = tempEnd
			else:
				prev.next = reverseTemp(tempStart, k)[0]
			isFirst = False
		else:
	return



l1 = ll.ListNode(1)
l2 = ll.listToLink([1, 2, 3, 4])
l3 = None
l4 = ll.listToLink([3, 2, 1, 5, 4, 3])
l5 = ll.listToLink(list(range(10)))
l6 = ll.listToLink(list(range(10)))

def testReverseLL():
	print(ll.printListNode(reverseLL(l1))) # 1
	print(ll.printListNode(reverseLL(l2))) # 4 -> 3 -> 2 -> 1
	print(ll.printListNode(reverseLL(l3))) # []--return an empty linkedlist
	print(ll.printListNode(reverseLL(l4))) # 3 -> 4 -> 5 -> 1 -> 2 -> 3

#testReverseLL()

def testReverseKGroup():
	print(ll.printListNode(reverseKGroup(l1, 1))) # 1
	print(ll.printListNode(reverseKGroup(l2, 4))) # 4 -> 3 -> 2 -> 1
	print(ll.printListNode(reverseKGroup(l3, 1))) # 1
	print(ll.printListNode(reverseKGroup(l5, 4))) # 3 -> 2 -> 1 -> 0 -> 7 -> 6 -> 5 -> 4 -> 8 -> 9
	print(ll.printListNode(reverseKGroup(l6, 6))) # 5 -> 4 -> 3 -> 2 -> 1 -> 0 -> 6 -> 7 -> 8 -> 9


testReverseKGroup()




