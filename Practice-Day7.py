import LinkedList as ll
'''
Question 20
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

'''
'''
Idea
- Keep track of the open "parantheses" with a stack (LIFO-last in, first out)
- With Python, this could be tracked through a list
	- Whenever we encounter an open paran, we append it to the list
	- If we see a closed paran, pop (get the last element in the list, which is the latest) and check against the closed paran
	- if matching, keep going till the end of the list. Else, invalid combo --> return false
- If we reach the end of the list, and the stack isn't empty, return false
'''

def isValid(s):
	mappings = {'(': ')', '[':']', '{':'}'} # Mappings of open to closed parans
	stack = [] # Functions as a stack--LIFO
	for char in s: # Iterate through the chars of the string
		if char in mappings: # Case where we have an open paran
			stack.append(char) # Add it to the stack
		else: # Case where we have a closed paran
			if not stack: # Case where there isn't any open paran--no match possible
				return False
			val = stack.pop() # Get the most recent open paran
			if mappings[val] != char:
				return False
	return not stack


def testIsValid():
	print(isValid('()')) # true
	print(isValid('()[]{}')) # true
	print(isValid('(]')) # false
	print(isValid('([)]')) # false
	print(isValid('{[]}')) # true
#testIsValid()

'''
Question 21

Merge two sorted linked lists and return it as a sorted list. The list should be made 
by splicing together the nodes of the first two lists.
'''

# Borrowing the LL infrastructure from day 2
l1 = ll.listToLink([1, 2, 4])
l2 = ll.listToLink([1, 3, 4])
l3 = ll.listToLink([])
l4 = ll.listToLink([])
l5 = ll.listToLink([])
l6 = ll.listToLink([0])


def mergeTwoLists(l1, l2):
	p1 = l1 # pointer to the first LL
	p2 = l2 # pointer to the second LL
	mergedLL = ll.ListNode(0)
	p3 = mergedLL
	while p1 or p2:
		#print('reached?')
		if not p1: # Case where we've iterated through all of the first linked list
			#print('case1')
			mergedLL.next = p2
			return p3.next
		elif not p2: # Case where we've iterated through all of the second linked list
			#print('case2')
			mergedLL.next = p1
			return p3.next
		else: # Need to check the values of each linked list against each other
			#print('case3')
			val1 = p1.val # Value in the first linked list
			val2 = p2.val # Value in second LL
			if val1 <= val2: # Case where the first LL is the smaller of equal of the 2
				mergedLL.next = ll.ListNode(val1) # Add the smaller value to the LL
				p1 = p1.next # Move to next value of the first LL
			else: # See above but for the 2nd LL
				mergedLL.next = ll.ListNode(val2)
				p2 = p2.next
		mergedLL = mergedLL.next # Move onto the end of the LL that we've constructed
		#print(ll.printListNode(p3))
	return p3.next

def testMergeTwoLists():
	print(ll.printListNode(mergeTwoLists(l1, l2))) # 1 -> 1 -> 2 -> 3 -> 4 -> 4
	print(ll.printListNode(mergeTwoLists(l3, l4))) # []--empty linked list
	print(ll.printListNode(mergeTwoLists(l5, l6))) # 0

#testMergeTwoLists()

'''
Question 22
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''

'''
Ideas
- We can first generate all possible sequences of length n with open and closed paranthesis
	- Then, we want to verify which of these are valid sequences
	- To be a valid sequence, the number of open and closed paranthesis when iterating through the sequence
	  must be net positive in favor of open paranthesis but at end of sequence it should be 0
- Improvement: stop generation of a sequence if invalid at any point
'''

def generateParanthesis(n):
	def generateSequence(lst):
		if len(lst) == 2 * n: # We have a sequence of the desired length
			if verifySequence(lst):
				sequences.append(''.join(lst)) # Add the sequence to the list in the string form
		else: # We don't have the desired length
			lst.append('(') # Case where we use an open paran
			generateSequence(lst) # Recurse... add to our sequence
			lst.pop() # Remove from the original list to create a new sequence
			lst.append(')') # Case where we have a closed paran to add to our sequence
			generateSequence(lst) # Recurse with the new sequence
			lst.pop() # Reset the list in respect to the latest element

	'''
	Under the new generate sequence, we only add when there's a valid sequence thus far. To prserve
	the validity of the sequence, we track the number of open and closed paran
	- So long as open < totalOpenPossible: add an open to existing sequence and increment counter for open
		- Add a closed paran if we have a valid sequence and increment the counter for closed parans
		- After each operation, need to pop the latest element to generate a new sequence
	'''
	def generateSequence2(lst, open, closed):
		if len(lst) == 2 * n: # We have a sequence of the desired length
			if verifySequence(lst):
				sequences.append(''.join(lst)) # Add the sequence to the list in the string form
		if open < n: # Need to make sure we haven't exceeded our quota of open paran
			lst.append('(') # Add an open paran
			generateSequence2(lst, open + 1, closed) # Recurse (knowing we have 1 more open paran)
			lst.pop() # Get rid of latest element
		if open >= closed: # Make sure we still have a valid sequence
			lst.append(')') # Add a closed paran
			generateSequence2(lst, open, closed + 1) # Recurse... knowing we have 1 more closed paran
			lst.pop() # Reset the last element
	# Helper method to verify a valid sequence
	def verifySequence(seq):
		balance = 0 # Keep track of the balance
		for char in seq: # Go through all the chars in a given sequence
			if balance < 0: # Balance is < 0
				return False # Return False
			if char == '(': # Increment upon open paranthesis
				balance += 1
			else: # Decrement upon closed paranthesis
				balance -= 1
		return balance == 0 # Ensure net balance == 0
	sequences = [] # List that we add all sequences of the desired length
	#generateSequence([])
	generateSequence2([], 0, 0)
	return sequences

def testGenerateParanthesis():
	print(generateParanthesis(3)) # ["((()))","(()())","(())()","()(())","()()()"]
	print(generateParanthesis(1)) # ['()']
#testGenerateParanthesis()


def mergeKLists(lists):
	mergedList = []
	for lst in lists:
		p = lst
		while p != None:
			mergedList.append(p.val)
			p = p.next
	mergedList.sort()
	
	mergedLL = ll.ListNode(0)
	p = mergedLL
	for val in mergedList:
		p.next = ll.ListNode(val)
		p = p.next
	return mergedLL.next

kl1 = [ll.listToLink([1, 4, 5]), ll.listToLink([1, 3, 4]), ll.listToLink([2, 6])]
kl2 = []
kl3 = [ll.ListNode(None)]
def testMergeKLists():
	print(ll.printListNode(mergeKLists(kl1))) # 1->1->2->3->4->4->5->6
	print(ll.printListNode(mergeKLists(kl2))) # [] --empty LL
	print(ll.printListNode(mergeKLists(kl3))) # [] --empty LL
testMergeKLists()









