'''
Question 11
Given n non-negative integers a1, a2, ..., an , where each represents a 
point at coordinate (i, ai). n vertical lines are drawn such that the 
two endpoints of the line i is at (i, ai) and (i, 0). Find two lines,
which, together with the x-axis forms a container, such that the container 
contains the most water.
'''

'''
Approach 1
- Iterate throughout the entire array, generate all combination of indices and find the respective
  areas using minValue b/w the relevant indices and multiply by the width
  - This is too slow
'''
def maxArea(arr):
	lenArr = len(arr)
	maxVal = 0
	for i in range(lenArr):
		for j in range(i+1, lenArr):
			maxVal = max(maxVal, min(arr[i], arr[j]) * (j - i))
	return maxVal




'''
Approach 2
- Start with a pointer at each end of the array
- Move inward according to which has the min value
	- Idea: the smaller of the 2 values can only be improved by moving inwrd
'''
def maxArea2(height):
	lenArr = len(height)
	maxVal = 0
	start = 0
	end = len(height) - 1
	while start < end:
		#print(start, end)
		startVal = height[start]
		endVal = height[end]
		#print(start, end, startVal, endVal)
		if startVal < endVal: # The starting pointer contains the lesser of the two
			area = startVal * (end - start)
			start += 1
		elif startVal > endVal: # Ending pointer contains the lesser of the values
			area = endVal * (end - start)
			end -= 1
		else: # Values are the same
			area = endVal * (end - start)
			start += 1 # Need to increment to next value of start
			end -= 1 # Decrement end pointer
		if area > maxVal:
			maxVal = area
		#maxVal = max(maxVal, area)
	return maxVal


def testMaxArea():
	print(maxArea2([1,8,6,2,5,4,8,3,7])) # min(8, 7) * 7 = 49
	print(maxArea2([1, 1])) # min(1, 1) * 1 = 1
	print(maxArea2([4, 3, 2, 1, 4])) # 16
	print(maxArea2([1,2,1])) # min(2, 1) * 1 = 2, min(1, 1) * 2 = 2
#testMaxArea()


# Find the maximal sum of a binary tree between unconnected nodes
'''
Assume we have a binary tree
root = [3,2,3,null,3,null,1] --> 7
root = [3,4,5,1,3,null,1] --> 9
'''

'''
Ideas
- We want to traverse this tree using BFS
- As such, we can sum as we go through the level
	- At a given level, there are 2^0 entries
'''

class Tree:
	def __init__(self, value = 0, right = None, left = None):
		self.val = value
		self.left = left
		self.right = right

'''
Improvements
- helper(t.left, True) calls helper(t.left, False) internally
	- Want some way of avoiding this repeat computation
'''

def maxRobberSum(tree):
	# Need a helper function to track whether parent was robbed
	def helper(t, robbedParent): # t = tree, robbedParent = true IFF the parent was robbed
		if t == None: # Base case: tree node is empty
			return 0 # Sum of 0
		else: # Need to recurse with remaining nodes
			if robbedParent: # The parent was robbed--meaning we can't rob the children
				return helper(t.left, False) + helper(t.right, False)
			else: # Parent wasn't robbed: can choose between robbing and not robbing
				#print('tval: ', t.val, t == None)
				rob = t.val + helper(t.left, True) + helper(t.right, True) # Calculate the robbed value
				notRobbed = helper(t.left, False) + helper(t.right, False) # Assume we didn't rob
				return max(rob, notRobbed)
	return helper(tree, False) # Use the helper function with the original tree

# Allow helper(node.left) to represent the return to [helper(node.left, parentRobbed), helper(node.left, not(parentRobbed))]
def maxRobberSum2(tree):
	def helper(t): # t = tree, robbedParent = true IFF the parent was robbed
		if t == None: # Base case: tree node is empty
			return (0, 0) # Sum of 0
		else:
			leftVal = helper(t.left) # Recurse and find the val associated with left tree
			rightVal = helper(t.right) # Recurse and find val associated with right tree
			rob = t.val + leftVal[1] + rightVal[1] # Incorporate current value and non-robbed sum of the children
			notRobbed = max(leftVal) + max(rightVal) # Choose the best option among the children of robbed vs. not robbed b/c didn't rob parent
			return (rob, notRobbed)
	return max(helper(tree)) # Use the helper function with the original tree, returning best option


t1 = Tree(3, Tree(2, None, Tree(3)), Tree(3, None, Tree(1)))
t2 = Tree(3, Tree(4, Tree(1), Tree(3)), Tree(5, None, Tree(1)))

# This can be further improved through memoization
'''
Central Idea
- We just use (treeID, robbedParent) as the key to track whether we have encountered a tree before
	- Will be building off of the original maxRobberSum implementation
'''
def maxRobberSum3(tree):
	memo = {} # This will contain the cache of memoized results
	# Need a helper function to track whether parent was robbed
	def helper(t, robbedParent): # t = tree, robbedParent = true IFF the parent was robbed
		if t == None: # Base case: tree node is empty
			return 0 # Sum of 0
		else: # Need to recurse with remaining nodes
			if (t, robbedParent) in memo:
				return memo[t, robbedParent]
			if robbedParent: # The parent was robbed--meaning we can't rob the children
				val = helper(t.left, False) + helper(t.right, False)
				memo[t, robbedParent] = val
			else: # Parent wasn't robbed: can choose between robbing and not robbing
				#print('tval: ', t.val, t == None)
				rob = t.val + helper(t.left, True) + helper(t.right, True) # Calculate the robbed value
				notRobbed = helper(t.left, False) + helper(t.right, False) # Assume we didn't rob
				val = max(rob, notRobbed)
				memo[t, robbedParent] = val
			return val
	return helper(tree, False) # Use the helper function with the original tree

def testMaxRobberSum():
	print(maxRobberSum(t1)) # 7
	print(maxRobberSum(t2)) # 9
	print(maxRobberSum2(t1)) # 7
	print(maxRobberSum2(t2)) # 9
	print(maxRobberSum3(t1)) # 7
	print(maxRobberSum3(t2)) # 9
testMaxRobberSum()


















