'''
Question 31

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted 
in ascending order).

The replacement must be in place and use only constant extra memory.

'''

'''
IDEA 0
- We could create all possible permutations of elements in the list and find the "optimal" arrangement that
  exceeds the current by the least amount

Idea 1
- Go through the remaining elements of the list and try to see how we can best sort remaining elements
	- See if there is a valid permutation that exceeds the current
	- Do we go 1 element at a time?

Algorithm
1. Need to find the first strictly decreasing element starting from the end of the list moving towards the front
2. Next, since we know that all the elements to the right are decreasing, find the element that is greateer than
the element found in 1 by the lowest amount.
3. Swap elements in step 1 and step 2
4. Sort all the remaining elements (in-place) to the right of the element found in 2 rightward

'''

# Helper method: swap elements in position pos1 and pos2
def swapElements(nums, pos1, pos2):
	temp = nums[pos1] # Find the temporary position
	nums[pos1] = nums[pos2] # Change 
	nums[pos2] = temp # And Change

# Helper method: reverse all the elements from start onward to the end of the list
def reverseList(nums, start):
	for i in range(int((len(nums) - start)/2)): # Iterate through half-length
		swapElements(nums, start + i, len(nums) - i - 1) # Swap the elements we need


# Such an unintuitive algorithm...
def nextPermutation(nums):
	end = len(nums) - 2 # Start at next to last element of the list
	while end >= 0 and (nums[end + 1] <= nums[end]): # While we haven't reached the front of the list + the successive element is greater
		end -= 1 # Decrement the counter
	if end >= 0: # So long as the list isn't already sorted
		swapIndex = len(nums) - 1 # Start at the end of the list
		while nums[swapIndex] <= nums[end]: # Start from end of list and find the closest greater element
			swapIndex -= 1 # Decrement
		swapElements(nums, end, swapIndex) # Perform the swap
	reverseList(nums, end + 1) # Sort the remaining elements

l1 = [1, 2, 3]
l2 = [3, 2, 1]
l3 = [1, 1, 5]
l4 = [1]
l5 = [1, 3, 4, 5, 2]
def testNextPermutations():
	nextPermutation(l1) # [1, 3, 2]
	print(l1)
	nextPermutation(l2) # [3, 2, 1]
	print(l2)
	nextPermutation(l3) # [1, 5, 1]
	print(l3)
	nextPermutation(l4) # [1]
	print(l4)
	nextPermutation(l5) # [1, 3, 5, 2, 4]
	print(l5)
#testNextPermutations()


'''
Question 32
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
'''

'''
Idea 1
- Iterate through the string, and each time we encounter an open paranthesis, add onto a dictionary
	- Each time the index hits zero, check to see if it is a longer sequence than previously encountered
	- Can also invalidate any open paran that becomes invalid (meaning that we have more closed than open)
'''

# Approach 1: Generate all possible sequences starting with open paran and check for validity --> longest valid wins

def lvp1(s):
	# Helper method to define a valid sequence
	def isValid(seq):
		count = 0
		for s in seq:
			if s == '(':
				count += 1
			else:
				count -= 1
			if count < 0:
				return False
		return count == 0
	n = len(s)
	longest = 0
	for i in range(n): # Go through the initial sequence
		for j in range(i + 2, n + 1): # Define the remaining elements--accommodate the last one
			#if i + 2 <= j:
			seq = s[i:j]
			if isValid(seq) and len(seq) > longest:
				longest = len(seq)
	return longest


'''
Approach 2: Set up an array of longest valid sequence that is attainable up until each index of the array
	- Case 1: last 2 elements encountered are () --> increment the count by 2
	- Case 2: last 2 elements are )):
		- Make sure that the inner sequence that's valid that is preceded by (
		- Inner sequence must be valid which we can add onto length of the string
		- Then add on longest sequence found so far pre-(SEQ))
		
'''
def lvp2(s):
	n = len(s)
	arr = [0] * n
	longest = 0 # Track the longest valid sequence
	for i in range(1, n):
		if s[i - 1] == '(' and s[i] == ')':
			arr[i] += 2 # Increment the total we've seen by 2 by ()
			longest = max(longest, arr[i])
		if s[i - 1] == ')' and s[i] == ')': # Case where we have )) for the last 2 elements
			temp = arr[i-1] # Get the longest sequence found by the element just prior
			if s[i - temp - 1] == '(': # Make sure that the element right before the longest valid sequence element prior is (
				longestPreTemp = arr[i - arr[i-1] - 2] # Get longest sequence pre-longest string just prior
				arr[i] = temp + 2 # Get LVP of previous + increment by 2 for surrounding () of the valid sequence
				longest = max(longest, arr[i])
	return max(longest, arr[i])


'''
Approach 3: Use a stack to push when we encounter an open paran, and push when we see a closed paran
	- If the stack is empty --> push the most recent element index (since we finished a "sequence")
	- If we find a ): take the difference b/w the value at the top of the stack from popped element


( ((()())) (
'''

def lvp3(s):
	stack = [-1] # Track the indices + longest sequence
	longest = 0 # Track longest
	for i in range(len(s)): # Go through the string
		if s[i] == '(': # Open paran case
			stack.append(i) # Add it to the list
		else: # Case where we have closed paran
			stack.pop() # Get rid of the most recent element from the stack
			if not stack: # Empty stack
				stack.append(i)
			else:
				seqLength = i - stack[-1] # Get the sequence length--based on the length we just saw
				longest = max(seqLength, longest) # Find longest sequence
	return longest


'''
Approach 4: take a forward and backward pass approach
- Forward pass: account for case where we have more )'s than ('s
	- Ex1: (((() illustrates necessity of backpass since the counter will not reach 0
- Backward pass: account for case when we have more ('s than )'s'
	- Ex2: ()))))) shows the above but for the forward pass's necessity
'''

def lvp4(s):
	longest = 0 
	# Forward Pass
	openCount, closedCount = 0, 0
	for i in range(len(s)):
		if s[i] == '(': # Encountered a closed paran
			openCount += 1
		else: # Otherwise, it's a closed paran
			closedCount += 1
		if openCount == closedCount: # Valid sequence
			longest = max(longest, openCount * 2) # Counts must be equal --> can double
		elif openCount < closedCount: # Too many closed parantheses relative to the open
			openCount, closedCount = 0, 0 # Reset counters

	# Backward Pass
	openCount, closedCount = 0, 0
	for i in range(len(s) - 1, 0, -1):
		if s[i] == ')': # Case where we start with closed paran
			closedCount += 1
		else: # Encountered an open paran
			openCount += 1
		if openCount == closedCount:
			longest = max(longest, openCount * 2) # Get the length of the sequence found so far
		elif closedCount < openCount: # Invalid sequence in backtrack metric
			openCount, closedCount = 0, 0 # Reset the counters
	return longest




s1 = '())(()))' # 4
s2 = '((())' # 4
s3 = '(()' # 2
s4 = ')()())' # 4
s5 = ')(()())))))(' # 6

# Testing the various versions--brute force, dynamic programming, stack, forward + backward pass
def testLVP():
	print(lvp1(s1))
	print(lvp1(s2))
	print(lvp1(s3))
	print(lvp1(s4))
	print(lvp1(s5))

	print(lvp2(s1))
	print(lvp2(s2))
	print(lvp2(s3))
	print(lvp2(s4))
	print(lvp2(s5))

	print(lvp3(s1))
	print(lvp3(s2))
	print(lvp3(s3))
	print(lvp3(s4))
	print(lvp3(s5))

	print(lvp4(s1))
	print(lvp4(s2))
	print(lvp4(s3))
	print(lvp4(s4))
	print(lvp4(s5))

testLVP()




