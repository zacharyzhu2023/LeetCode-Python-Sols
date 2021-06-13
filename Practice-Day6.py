'''
Question 17
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''


'''
Ideas
- Generate a mapping from each digit to each possible letter (stored in a set)
- From there, iterate through the length of digits
	- Assign an element each time
'''

def letterCombinations(digits):
	mappings = {
	'2': {'a', 'b', 'c'},
	'3': {'d', 'e', 'f'},
	'4': {'g', 'h', 'i'},
	'5': {'j', 'k', 'l'},
	'6': {'m', 'n', 'o'},
	'7': {'p', 'q', 'r', 's'},
	'8': {'t', 'u', 'v'},
	'9': {'w', 'x', 'y', 'z'},
	}
	n = len(digits)
	if n == 0: # Base case: no digits
		return []
	elif n == 1: # Use the mappings directly for a single digit
		return list(mappings[digits])
	elif n == 2: # Use mappings w/ 2 digits
		first = mappings[digits[0]]
		second = mappings[digits[1]]
		return [a + b for a in first for b in second]
	elif n == 3: # Use mappings w/ 3 digits
		first = mappings[digits[0]]
		second = mappings[digits[1]]
		third = mappings[digits[2]]
		return [a + b + c for a in first for b in second for c in third]
	else: # Use the mapping with 4 digits
		first = mappings[digits[0]]
		second = mappings[digits[1]]
		third = mappings[digits[2]]
		fourth = mappings[digits[3]]
		return [a + b + c + d for a in first for b in second for c in third for d in fourth]

# Alternate Solution to accommodate having >4 letters
def letterCombinations2(digits):
	mappings = {
	'': [],
	'2': ['a', 'b', 'c'],
	'3': ['d', 'e', 'f'],
	'4': ['g', 'h', 'i'],
	'5': ['j', 'k', 'l'],
	'6': ['m', 'n', 'o'],
	'7': ['p', 'q', 'r', 's'],
	'8': ['t', 'u', 'v'],
	'9': ['w', 'x', 'y', 'z'],
	}
	def helper(digits): # Helper method that using mappings to generate list of combinations
		if digits in mappings: # Return digits if already in mappings
			return mappings[digits]
		else:
			newMapping = [] # Create a mapping
			remaining = helper(digits[1:]) # Get combinations for remaining digits w/ recursive call
			for char in mappings[digits[0]]: # Get the given first digit possibilities
				for comb in remaining: # Go through the combinatinos of the remaining digits
					newMapping.append(char + comb) # Add the combination of the 2
			mappings[digits] = newMapping # Add mapping to existing mapping
			return newMapping # Return the newMapping that was generated under helper w/ recursive call 
	return helper(digits) # Call helper with the original digits list

def testLetterCombinations():
	print(letterCombinations('23')) # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
	print(letterCombinations('2')) # ['a', 'b', 'c']
	print(letterCombinations('')) # []
	print(letterCombinations2('23')) # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
	print(letterCombinations2('2')) # ['a', 'b', 'c']
	print(letterCombinations2('')) # []
#testLetterCombinations()



'''
Question 18
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
'''

'''
Ideas
- Could we borrow from the 3sum approach?
- First, sort the list
- Iterate through nums the first time around, with a second pointer starting at an element right after the first pointer
	- Then apply the START, END pointer approach to analyze fourSum
	- If matching target and not in original set (sort the solution), add it to the list of solutions
'''

def fourSum(nums, target):
	nums.sort() # Sort list: O(log(n))
	n = len(nums) # Length of nums list
	sols = [] # List of unique sols
	for i in range(n-2): # First round of iteration
		for j in range(i+1, n - 2): # Second round of iteration
			start  = j + 1 # Third index
			end = n - 1 # Fourth index
			while start < end: # Keep iterating so long as we don't cross to smaller/larger values
				vals = [nums[i], nums[j], nums[start], nums[end]] # Get the current combination of values
				sumVals = sum(vals) # Find the sum of a given combination
				if sumVals == target: # Target met?
					if vals not in sols: # Check to see if we already have this given solution
						sols.append(vals) # If not, add it to the given solutions
					start += 1 # Increment start b/c if we change start or end alone, either get a repeat or non-target value
					end -= 1 # See above
				elif sumVals < target: # Need a greater sum
					start += 1
				else: # Need a smaller sum
					end -= 1
	return sols

def fourSumTest():
	print(fourSum([1,0,-1,0,-2,2], target = 0))
	print(fourSum([2, 2, 2, 2, 2], target = 8))

#fourSumTest()

'''
Question 19
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''

'''
Ideas
- First go through the entire linked list to get the length of the list
	- In the second pass of the linked list, gets rid of the nth-from-end and attach to rest of list

'''

# Importing LinkedList class from Day2
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

# 2 Pass Approach
def removeNthFromEnd(head, n): # head is the beginning of the linked list, n is the how far we are from the end
	if head == None or head.next == None: # Base case
		return None
	lenList = 0 # Get the length of the overall list
	pointer = head
	while pointer != None:
		pointer = pointer.next # Point at next instance
		lenList += 1 # Increment length of list
	index = lenList - n # Get index to remove
	#print('index:', index)
	if index == 0: # Need to account for case where we want to get rid of the first element of a linked list
		return head.next
	pointer2 = head # Get another pointer
	counter = 0 # Increment through the linked list
	while counter + 1 < index: # Iterate through linked list using the new pointer
		pointer2 = pointer2.next # Go through the linked list again
		counter += 1
	#print('pointer2:', printListNode(pointer2))
	pointer2.next = pointer2.next.next # Get rid of the given element
	return head

# Alt approach 2: use 2 pointers at the same time
def removeNthFromEnd2(head, n):
	pointer0 = ListNode(0) # Create a new listNode that will reference head
	pointer0.next = head
	pointer1 = pointer0 # First pointer
	pointer2 = pointer0 # Second Pointer
	counter = 1 # Want to create a "distance" between the 2 pointers
	while counter <= n + 1: # Create a gap of 2 + 1 for each additional point we want to go from the end
		pointer2 = pointer2.next # Increment what pointer2 points to create the gap
		counter += 1
	#print('pointer1:', printListNode(pointer1))
	#print('pointer2:', printListNode(pointer2))
	while pointer2 != None: # Want to transfer pointer1 + pointer2 to maintain the gap
		pointer1 = pointer1.next # Move the first pointer (will be one before the element we want to remove)
		pointer2 = pointer2.next # pointer2 moves in tandem
	#print('pointer1:', printListNode(pointer1))
	#print('pointer2:', printListNode(pointer2))
	pointer1.next = pointer1.next.next
	#return head
	#print('head:', printListNode(head))
	#print('pointer0.next:', printListNode(pointer0.next))
	return pointer0.next 
l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
l2 = ListNode(1, ListNode(2))
l3 = ListNode(1, ListNode(2))
l4 = listToLink([3, 4, 5, 6])
l5 = listToLink([3, 4, 5, 6])
ll1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
ll2 = ListNode(1, ListNode(2))
ll3 = ListNode(1, ListNode(2))
ll4 = listToLink([3, 4, 5, 6])
ll5 = listToLink([3, 4, 5, 6])
l01 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
l02 = ListNode(1, ListNode(2))
l03 = ListNode(1, ListNode(2))
l04 = listToLink([3, 4, 5, 6])
l05 = listToLink([3, 4, 5, 6])

# Alt Approach 3: using 2 pointers w/o creating a new linked list
def removeNthFromEnd3(head, n):
	counter = 1 # Counter to create distance
	pointer1 = pointer2 = head # One pointer for element to remove, another to create distance
	while pointer2.next != None:
		pointer2 = pointer2.next # This will be moved to create distance from the head
		counter += 1
		if counter > n + 1: # We've created sufficient distance
			pointer1 = pointer1.next # Pointer1 will point to the element right before the one we want to remove
	if counter == n: # Account for case where we only want to remove first element
		return head.next # There's no "next" element we want to modify
	else:
		pointer1.next = pointer1.next.next
		return head

def testRemoveNthFromEnd():
	print(printListNode(removeNthFromEnd(l1, 2))) # 1 -> 2 -> 3 -> 5
	print(printListNode(removeNthFromEnd(l2, 1))) # 1
	print(printListNode(removeNthFromEnd(l3, 2))) # 2
	print(printListNode(removeNthFromEnd(l4, 4))) # 4 -> 5 -> 6
	print(printListNode(removeNthFromEnd(l5, 1))) # 3 -> 4 -> 5

	print(printListNode(removeNthFromEnd2(ll1, 2))) # 1 -> 2 -> 3 -> 5
	print(printListNode(removeNthFromEnd2(ll2, 1))) # 1
	print(printListNode(removeNthFromEnd2(ll3, 2))) # 2
	print(printListNode(removeNthFromEnd2(ll4, 4))) # 4 -> 5 -> 6
	print(printListNode(removeNthFromEnd2(ll5, 1))) # 3 -> 4 -> 5

	print(printListNode(removeNthFromEnd3(l01, 2))) # 1 -> 2 -> 3 -> 5
	print(printListNode(removeNthFromEnd3(l02, 1))) # 1
	print(printListNode(removeNthFromEnd3(l03, 2))) # 2
	print(printListNode(removeNthFromEnd3(l04, 4))) # 4 -> 5 -> 6
	print(printListNode(removeNthFromEnd3(l05, 1))) # 3 -> 4 -> 5

#testRemoveNthFromEnd()







