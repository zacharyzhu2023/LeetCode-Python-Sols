'''
Question 14
Write a function to find the longest common prefix string amongst an array
of strings. If there is no common prefix, return an empty string "".
'''

'''
Idea
- Do we just iterate throughout each of the strings and access the each one index at a time
	- Runtime: N = length of strs, M = min length of a string in strs
	- Worst case scenario, we need to go through all the strings and use the shortest length string
	- O(MN) for the runtime
'''


def longestCommonPrefix(strs):
	counter = 0 # Counter to access elements of each string individually
	minLength = min({len(s) for s in strs}) # Find the minimum length string in strs
	lcp = '' # This is the longest common prefix
	while counter < minLength and all([s[counter] == strs[0][counter] for s in strs]):
		lcp += strs[0][counter] # Building the string of LCP
		counter += 1 # Incrementing the counter
	return lcp

def testLCP():
	print(longestCommonPrefix(["flower","flow","flight"])) # fl
	print(longestCommonPrefix(["dog","racecar","car"])) # ''

#testLCP()

'''
Question 15
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''

'''
Approach 1: Iterate thrice throughout nums to get the triples
- Make sure that the triples are unique + sorted, and if the sum is zero
	- If not, move onto the next triple
- This is inefficient b/c it requires iterating thrice throughout the list
- Runtime: O(n^3)
'''
def threeSum(nums):
    sols = [] # Build a list that constructs all unique triples
    for i in range(len(nums)): # Iterate throughout the list
        for j in range(i+1, len(nums)): # Go through remaining elements
            for k in range(j+1, len(nums)): # Go through last set of elements
                temp = [nums[i], nums[j], nums[k]] # what is the triple?
                temp.sort() # Sort the list
                #print(temp, sum(temp), temp in sols)
                if (sum(temp) == 0 and not(temp in sols)): # Should we include the triple
                    sols.append(temp)
    return sols

'''
- First, we sort the original array of numbs
- Then, we pick an element as our anchor (iterating throughout the array)
	- Among the remaining elements that are greater than the anchor, we want to see if 3sum is possible
	- We have a pointer to start from the low end and the high end
	- 3 possible cases: sum = 0, sum < 0, sum > 0
		1. sum = 0: add to list of sol's + increment lower counter, decrement upper counter
		2. sum < 0: increment lower counter (try to achieve a greater overall sum)
		3. sum > 0: decrement upper counter (try to get a lower overall sum)

- Sorting is a O(log(n)) operation
- Looping through the first list is a O(n) operation
	- Then, we iterate through remaining elements (a single time in essence)
- This becomes a O(n^2 + log(n)) operation in total --> O(n^2) since log(n) gets eclipsed
'''

def threeSum2(nums):
	nums.sort()
	sols = []
	for i in range(len(nums) - 2):
		start = i + 1
		end = len(nums) - 1
		while start < end:
			sumVals = nums[i] + nums[start] + nums[end]
			if sumVals == 0: # Case where sum == 0
				valList = [nums[i], nums[start], nums[end]]
				if not(valList in sols):
					sols.append(valList)
				start += 1
				end -= 1
			elif sumVals < 0: # Case where sum < 0
				start += 1
			else: # Case where sum > 0
				end -= 1
	return sols

def twoSum(nums, target): # Return list of all unique doubles that return a sum of target
	sols = set() # Initialize an empty set
	#print('nums', nums, 'target', target)
	for i in range(len(nums)): # Iterate through all the eleemnts
		val = nums[i] # Find the current value
		remainder = target - val # What is the remaining value that we'd need to reach the target?
		#print('sols', sols, 'tuple', (val, remainder))
		if val > remainder and remainder in nums: # Make sure we don't have duplicates: append (greater, lower)
			sols.add((val, remainder)) # Make sure we don't have duplicates implicitly
		elif val < remainder and remainder in nums: # Add (greater, lower) in the other way around
			sols.add((remainder, val))
		elif val == remainder and nums.count(val) > 1:
			sols.add((remainder, val))
	return sols

def threeSum3(nums):
	# print(nums)
	# print(nums1)
	sols = []
	for i in range(len(nums)): # Iterate through all the elements
		currVal = nums[i] # Current value in nums
		#print(i, currVal)
		otherSums = twoSum(nums[i+1:], -currVal)
		possibleTuples = [sorted((currVal, double[0], double[1])) for double in otherSums]
		sols += [list(t) for t in possibleTuples if list(t) not in sols ]
	return sols

nums1 = [-1,0,1,2,-1,-4] # [[-1,-1,2],[-1,0,1]]
nums2 = [] # []
nums3 = [0] # []
nums4 = [-1, -1, 4, -2, -3, 0, 3]

def testThreeSum():
	# Test first solution
	print(threeSum(nums1))
	print(threeSum(nums2))
	print(threeSum(nums3))
	print(threeSum(nums4))

	# Test second solution
	print(threeSum2(nums1))
	print(threeSum2(nums2))
	print(threeSum2(nums3))
	print(threeSum2(nums4))

	# Test third solution
	print(threeSum3(nums1))
	print(threeSum3(nums2))
	print(threeSum3(nums3))
	print(threeSum3(nums4))


#testThreeSum()

# Question 16
'''
Given an array nums of n integers and an integer target, find three integers 
in nums such that the sum is closest to target. Return the sum of the three 
integers. 

You may assume that each input would have exactly one solution.
'''
# Naive solution: generate all possible triples
def threeSumClosest(nums, target):
	closest = float('inf')
	closestSum = 0
	for i in range(len(nums)):
		for j in range(i+1, len(nums)):
			for k in range(j + 1, len(nums)):
				tempSum = nums[i] + nums[j] + nums[k]
				#print('triple:', nums[i], nums[j], nums[k], tempSum)
				newDif = target - tempSum # Find the difference b/w the target and the sum
				#print('newDif:', newDif)
				if abs(newDif) < closest: # Only change the difference when we have a better sol
					#print('BETTER:', tempSum, abs(newDif))
					closestSum = tempSum
					closest = abs(newDif)
	return closestSum

# Can we improve upon this solution?
'''
Ideas
- Perhaps again we could sort the list, a O(log(n)) operation
- Then, we still have to iterate throughout the entire list
	- Then, we pick an anchor and iterate from the end of the list and the beginning of the list (list referring to the remaining elements)
	- From there, we can just go through the elements and pick whenever we encounter a lower 3sum value similar to the original 3sum probelm
'''

def threeSumClosest2(nums, target):
	nums.sort() # Sort the list w/o occupying more space
	#print('list', nums)
	closest = float('inf') # Find 
	closestSum = 0
	n = len(nums) # Get length of the list
	for i in range(n): # Iterate throughout the original nums list
		start = i + 1 # Get second element
		end = n - 1 # Mark third element
		while start < end:
			#print('triple: ', nums[i], nums[start], nums[end])
			tempSum = nums[i] + nums[start] + nums[end]
			if tempSum == target: # Case where we found the exact matching triple
				return target
			elif tempSum < target: # Case where triple sum is less than target
				if abs(tempSum - target) < closest:
					closest = abs(tempSum - target) # Alter closest value
					closestSum = tempSum # Change the closest sum--nearest to the target
				start += 1 # Want a greater value of the triple
			else: # Case where triple sum is greater than the target
				if abs(tempSum - target) < closest: 
					closest = abs(tempSum - target) # See above
					closestSum = tempSum
				end -= 1 # Want a smaller value for the triple sum
	return closestSum


def testThreeSumClosest():
	print(threeSumClosest([-1,2,1,-4], 1)) # 2 = -1 + 2 + 1
	print(threeSumClosest([-7, -8, -9, -3, -4], -20)) # -8 + (-9) + (-3) = -20
	print(threeSumClosest([-7, -8, -9, -3, -4, -5, -6], 0)) # -3 + (-4) + (-5) = -12
	print(threeSumClosest([-7, -8, -9, -3, -4, -12, -5, -6], -200)) # -8 + (-9) + (-12) = -29
	print(threeSumClosest2([-1,2,1,-4], 1)) # 2 = -1 + 2 + 1
	print(threeSumClosest2([-7, -8, -9, -3, -4], -20)) # -8 + (-9) + (-3) = -20
	print(threeSumClosest2([-7, -8, -9, -3, -4, -5, -6], 0)) # -3 + (-4) + (-5) = -12
	print(threeSumClosest2([-7, -8, -9, -3, -4, -12, -5, -6], -200)) # -8 + (-9) + (-12) = -29
testThreeSumClosest()




