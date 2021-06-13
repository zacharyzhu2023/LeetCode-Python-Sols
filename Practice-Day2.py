''' 2: Medium You are given two non-empty linked lists representing two non-negative integers. The
digits are stored in  reverse order, and each of their nodes contains a single digit. Add the two
numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

[2, 4, 3], [5, 6, 4] --> [7, 0, 8] using: 342 + 465 = 807
'''
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


l11 = ListNode(2, ListNode(4, ListNode(3)))
l12 = ListNode(5, ListNode(6, ListNode(4)))
l21 = ListNode(0)
l22 = ListNode(0)
l31 = listToLink([9, 9, 9, 9, 9, 9, 9])
l32 = listToLink([9, 9, 9, 9])
l41 = listToLink([9, 8, 7, 6, 5])
l42 = listToLink([1, 1, 1, 1, 5])
def testPrintLL():
	print(printListNode(l21))
	print(printRecursiveLL(l22))
	print(printListNode(l11))
	print(printRecursiveLL(l11))
	print(printListNode(l32))

# Iterative Solution
def addTwoNumbers(l1, l2):
	sumLL = ListNode(0)
	pointer = sumLL
	carryOver = 0
	while l1 != None or l2 != None or carryOver == 1:
		#print(l1.val, l2.val, carryOver)
		val1, val2 = 0, 0
		if l1 != None:
			val1 = l1.val
			l1 = l1.next
		if l2 != None:
			val2 = l2.val
			l2 = l2.next
		sumLL.val = (val1 + val2 + carryOver) % 10
		carryOver = int((val1 + val2 + carryOver) >= 10)
		if l1 != None or l2 != None or carryOver == 1:
			sumLL.next = ListNode()
			sumLL = sumLL.next
		
	return pointer

def testAddTwoNumbers():
	print(printListNode(addTwoNumbers(l11, l12)))
	print(printListNode(addTwoNumbers(l21, l22)))
	print(printListNode(addTwoNumbers(l31, l32)))



# Question 3: Find longest substring w/o repeating characters
'''
abcabcbb --> abc (length 3)
bbbbb --> b (length 1)
pwwkew --> wke (length 3)
"" --> 0

Initial Approach
- From each character, generate a substring
	- Create a set made up of all the characters in a given relevant substring
	- Keep adding onto that subset so long as the length improves and the original length meets or exceeds the best size encountered so far
	- Create the substring based off of the length of the best set encountered so far
'''
def lengthLongestSubstring(s):
	if len(s) == 0 or len(s) == 1: # Base case
		return len(s)
	else:
		longestSub, pos = 1, 0 # Set a startin position and the position for a substring
		substringSet = {}
		while longestSub + pos < len(s):
			substringSet = set(s[pos: pos + longestSub]) # Starter substring set
			if len(substringSet) < longestSub:
				pos += 1
			else:
				newPos = pos + longestSub # Get the position to build the substring
				prevSize = 0
				newSize = 1
				while newSize > prevSize and newPos < len(s):
					prevSize = len(substringSet) # Get PREVIOUS number of unique characters
					substringSet.add(s[newPos]) # Add in another char
					newSize = len(substringSet) # Get NEW number of unique elements
					newPos += 1
				longestSub = newSize 
				pos += 1
	return longestSub

def testLengthLongestSubstring():
	print(lengthLongestSubstring('abcabcbb'))
	print(lengthLongestSubstring('bbbbb'))
	print(lengthLongestSubstring('pwwkew'))
	print(lengthLongestSubstring(''))
	print(lengthLongestSubstring('au'))

#testLengthLongestSubstring()



# Sidenote: sliding window approach 

''' - This technique allows to avoid doing repeat work - Assume we are given the following array: 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] and wanted to compute the sum 5 elements at a time
- Sum 1: 1 + 2 + 3 + 4 + 5, Sum 2: 2 + 3 + 4 + 5 + 6
	- Instead of computing each sum manually each time, we can take the first sum, subtract one, and
	  add 6 to repeat doing as much comutation
- Reaps more benefits if we have larger k and larger n (avoid doing a lot of work)
 '''

 # Given a list of length n >= k, return sum of k-consecutive elements in the list
def getSumConsecutiveK(lst, k):
	listSum = []
	firstSum = sum(lst[:k]) # Get the sum of the first k elements
	listSum.append(firstSum) # Add it to the initial list
	for i in range(1, len(lst) - k + 1): # Iterate through remaining combos of the list
		firstSum += -1 * lst[i-1] + lst[i + k - 1] # Subtract the previous, add the newest
		listSum.append(firstSum) # Add in the new element
	return listSum

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]

def testGetSumConsecutiveK():
	testList = list(range(15))
	print(getSumConsecutiveK(testList, 3))
	print(getSumConsecutiveK(testList, 5))
	print(getSumConsecutiveK(testList, 7))
#testGetSumConsecutiveK()

'''
enumerate(): convert a collection to an enumerate object (has a counter)
'''

# Applying the sliding windows approach to longestSubstring
def longestSlidingWindow(s):
	longest, pos = 0, 0
	charsSeen = set()
	for r, c in enumerate(s): # r provides the position of the current char we're interested in
		if c in charsSeen: # Check to see if the char, c, at position r has been seen before
			#print('removed: ', pos, s[pos])
			charsSeen.remove(s[pos])
			pos += 1
		charsSeen.add(c)
		longest = max(longest, len(charsSeen))
	return longest

def testLongestSlidingWindows():
	print(longestSlidingWindow('abcabcbb'))
	print(longestSlidingWindow('bbbbb'))
	print(longestSlidingWindow('pwwkew'))
	print(longestSlidingWindow(''))
	print(longestSlidingWindow('au'))

#testLongestSlidingWindows()
'''
set() 0 a: start out empty, enumerate position 0 element is a (add it)
{'a'} 1 b: no chars to remove, so we can diretly add b
{'a', 'b'} 2 c: we add c, realizing no elements need to be removed
{'a', 'c', 'b'} 3 a: we add a, realize there was no benefit, so we get rid of the initial 0, a
{'a', 'c', 'b'} 4 b: we add b, realize there was no need, so get rid of the 1st element (whichw as b)
{'a', 'c', 'b'} 5 c: carry on the same process
{'a', 'c', 'b'} 6 b
{'c', 'b'} 7 b
removed:  5 c (on the last iteration, we need to remove both c and b since we're checking a string of length 1
removed:  6 b
'''


# Problem 4 (hard): find the median of 2 sorted arrays
# Caveat: need a runtime of log(m + n)
'''
Initial thoughts
- The naive way would be to merge the 2 arrays of size m and n, and then find the median
	- However, this would be O(m + n) since this would inspect every element of each array to add to a new array
'''

# Sol 1: Use extend which is O(n) and sort, which is O(log(m+n))
def findMedianSortedArrays(nums1, nums2):
	nums1.extend(nums2) # O(n) operation
	nums1.sort() # O(log(m+n)) operation (occurs behind the hood)
	if len(nums1) % 2 == 1: # O(1)--case where we're working with a list of odd length
		return nums1[len(nums1)//2] # Return the middle element
	else: # Working with a list of an even length
		return (nums1[len(nums1)//2 - 1] + nums1[len(nums1)//2])/2 # Return the average

def testFindMedianSorted():
	print(findMedianSortedArrays([1, 3], [2]))
	print(findMedianSortedArrays([1, 2], [3, 4]))
	print(findMedianSortedArrays([], [1]))
	print(findMedianSortedArrays([1, 5], [0, 3, 7, 8]))

#testFindMedianSorted()


# Sol 2: Perform binary search on the smaller of the two arrays
''' By performing search on the smaller of the 2 arrays and allowing the other array to
respond in kind, this becomes: O(log(min(m, n))) since binary search normally is O(k)

'''

def findMedianSorted2(nums1, nums2):
	len1, len2 = len(nums1), len(nums2) # What are the length of the respective lists?
	if len1 <= len2:
		low, high = 0, len1 # low + high index for binary search
		mid = (len1 + len2 + 1)//2 # What would the median index of the merged array be?
		while True:
			midX = low + (high - low)//2 # Find the location of median index of elements remaining
			midY = mid - midX # What is the median index of Y relative to the moving location of median of X
			# Need to check boundaries below to ensure we don't drift into the other array
			xLeft = nums1[midX - 1] if midX >0 else -1 * 999999# Get lower val of the 2 needed to compute median
			xRight = nums1[midX] if midX < len1 else 999999# Get upper val of the 2 needed to find median of X
			yLeft = nums2[midY-1] if midY > 0 else -1 * 999999 # See above but for Y
			yRight = nums2[midY] if midY < len2 else 999999 # See above but for Y
			if xLeft <= yRight and yLeft <= xRight: # Stopping condition: x lower bound <= y upper bound AND ylower <= xupper
				if (len1 + len2) % 2 == 1: # Single median value case
					return max(xLeft, yLeft)
				else: # Need 2 values to compute median case
					return (min(xRight, yRight) + max(xLeft, yLeft))/2
			elif xLeft > yRight:
				high = midX # Need to get a lower value of X (need a lesser index for the median of X)
			else:
				low = midX + 1 # X is too low: need to adjust the median index for X upward
	else:
		return findMedianSorted2(nums2, nums1) # Flip the order of the arrays--O(1) operation

def testMedianSorted2():
	print(findMedianSorted2([1, 3], [2]))
	print(findMedianSorted2([1, 2], [3, 4]))
	print(findMedianSorted2([], [1]))
	print(findMedianSorted2([1, 5], [0, 3, 7, 8]))

#testMedianSorted2()






