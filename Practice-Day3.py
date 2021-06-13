# Question 5: find thelongest palindromic substring in string s
'''
babad --> bab
cbbd --> bb
a --> a
ac --> a
'''

'''
Ideas
- Iterate throughout the string
	- Starting at a given index, expand to locate the longest possible palindrome
		- This can be broken down into 2 cases: even length and odd length palindrome
		- Even length: check 2 consecutive indices at a time
		- Odd length: check the 2 surrounding indices for a given index
abaaaa
'''

def longestPalindrome(s):
	strLen = len(s)
	if strLen == 1:
		return s
	# Even case
	longestPal, longestStr = 0, ''
	for i in range(0, strLen - 1):
		lenPalindrome, palindromeString  = 0, ''
		offset, matched = 0, True
		while i - offset >= 0 and i + offset + 2 <= strLen and matched:
			
			lowerChar = s[i - offset]
			upperChar = s[i + offset + 1]
			if lowerChar == upperChar:
				palindromeString = lowerChar + palindromeString + lowerChar
				lenPalindrome += 2
				offset += 1
			else:
				matched = False
		if lenPalindrome > longestPal:
			longestPal = lenPalindrome
			longestStr = palindromeString
	# Odd case
	for i in range(strLen):
		lenPalindrome, palindromeString  = 1, s[i]
		offset, matched = 1, True
		while i - offset >= 0 and i + offset < strLen and matched:
			#print('offset vals: ', i - offset, i + offset, s)
			lowerChar = s[i - offset]
			upperChar = s[i + offset]
			if lowerChar == upperChar:
				palindromeString = lowerChar + palindromeString + lowerChar
				lenPalindrome += 2
				offset += 1
			else:
				matched = False
		if lenPalindrome > longestPal:
			longestPal = lenPalindrome
			longestStr = palindromeString
	return longestStr

def testLongestPalindrome():
	print(longestPalindrome('babad'))
	print(longestPalindrome('cbbd'))
	print(longestPalindrome('a'))
	print(longestPalindrome('ac'))
	print(longestPalindrome('aaccabbacde'))
# testLongestPalidrome()

# Subproblem: find the longest common substring--FLAWED
def longestCommonSubstring(s1, s2):
	m = len(s1) # Get length of first string
	n = len(s2) # Get length of second string
	lengthLongest = 0 # Length of longest common substring
	longestStringsSet = set() # Create a set of all possible longest substrings
	counter = [[0] * (n+1) for i in range(m+1)] # Initialize a counter matrix to track when each char aligns within each substring
	for i in range(m): # Iterating throughout the second string
		for j in range(n): # Iterating throughout the first string
			if s1[i] == s2[j]: # This means that the characters for both strings align at a given position
				c = counter[i][j] + 1 # Increment the amount of common characters seen by 1
				counter[i+1][j+1] = c # Update the diagonal right-downward value to indicate for next iteration that a common character was found
				if c > lengthLongest: # We are working with a new longest string
					longest = c # c is the new longest length
					longestStringsSet.clear() # Clear the original set of strings
					longestStringsSet.add(s1[i-c+1:i+1]) # Track the substring values relative to position in s1
				elif c == lengthLongest:
					print('what is it?', s1[i-c+1:i+1])
					longestStringsSet.add(s1[i-c+1:i+1])
	return longestStringsSet

def lcsFixed(s1, s2):
	m = len(s1) # Get length of first string
	n = len(s2) # Get length of second string
	lengthLongest = 0 # Length of longest common substring
	longestString = ''
	for i in range(m): # Iterating throughout the second string
		for j in range(n): # Iterating throughout the first string
			counter = 0 # Counter to help create a matching substring
			matchedString = '' # At current i/j vals--create the longest possible common substring
			while ((i + counter < m) and (j + counter < n) and (s1[i + counter] == s2[j + counter])):
				matchedString += s1[i + counter] # If a given character matches, update the matched string
				counter += 1 # Increment the counter
				if len(matchedString) > len(longestString):
					longestString = matchedString
	return longestString


# print(longestCommonSubstring('academy', 'abracadabra'))
# print(longestCommonSubstring('ababc', 'abcdaba'))
# print(longestCommonSubstring('abcdefg', 'tuurriabee'))
# print(longestCommonSubstring('tuurriabee', 'abcdefg'))
# print(longestCommonSubstring('ababcbcbcbc', 'tuurriabcbaie9'))
def testLCS():
	print(lcsFixed("dd apple pie available", "apple pies"))
	print(lcsFixed('academy', 'abracadabra'))
	print(lcsFixed('ababc', 'abcdaba'))
	print(lcsFixed('abcdefg', 'tuurriabee'))
	print(lcsFixed('tuurriabee', 'abcdefg'))
	print(lcsFixed('ababcbcbcbc', 'tuurriabcbaie9'))
# testLCS()

# Question 6: ZigZag Conversion
'''

PAYPALISHIRING, numRows = 3 --> 
- We know this will get broken down into 3 divisions
	- First row: all characters that obey pos % 4 == 0
	- Second row: pos % 2 == 1 (alternatively, pos % 4 == 1, pos % 4 == 3)
	- Third row: pos % 4 == 2
0, 4, 8, 12
1, 3, 5, 7, 9, 11, 13
2, 6, 10
P   A   H   N
A P L S I I G
Y   I   R
--> PAHNAPLSIIGYIR

PAYPALISHIRING, numRows = 4 --> 

P     I    N
A   L S  I G
Y A   H R
P     I
- Cycle of 6 (how does numRows relate to the cycle length?)
	- 2 rows: cycle = 2, 3 rows: cycle = 4, 4 rows: cycle = 6
	- General rule of thumb: cycle = 2 * (numRows - 1)
	- First row: pos % cycle = 0
	- 2nd-all before last row: pos % cycle == rowNum or pos % cycle == -rowNum (accomplished w/ cycle - rowNum)
	- Last row: pos % cycle == cycle//2
--> PINALSIGYAHRPI

'''

'''
Ideas
- Naive approach: create a matrix (height = numRows, width = length original string)
- From there, can populate that matrix with the relevant values
	- The empty values can just be an empty string
- After fully population said matrix, can combine all the strings together from each row and each column
  by iterating through each possible entry

- Better approach: take advantage of the repeating based off of the "zig zag" structure
- Improvement to better approach: could use a dictionary to track which list each belonged to
	- From there, we would track direction (whether it was downward or upward)
	- Once the mod value hit numRows or 0 --> change directions
	- Can also convert a string into an iterable object (using StopIteration to stop looking for next)
'''

def zigzagConversion(s, numRows):
	if numRows == 1: # Base case: numRows == 1 means we can return original string
		return s
	lenStr = len(s) # Get the length of the string
	cycle = 2 * (numRows - 1) # Generate the cycle length based on number of rows
	halfCycle = cycle//2 # Get the half length of a cycle to avoid repeat computation
	convertedString = [''] * numRows # Populate a list of empty strings in most efficient way possible
	#print('converted: ', convertedString)
	for i in range(lenStr): # Iterate throughout the original string
		modVal = i % cycle # Which string do we want to build?
		if modVal == 0 or modVal == halfCycle or i % cycle < halfCycle:
			'''
			This covers 3 cases: working with first row, last row, or working our way downward in cycle before second half
			'''
			#print('val: ', i)
			convertedString[modVal] += s[i] # Can use the current mod value
		else:
			convertedString[cycle - modVal] += s[i] # We're working way back upward in cycle: must subtract off mod
	return ''.join(convertedString) # Most efficient way to convert a list of strings into a string

def testZigzagConversion(): 
	print(zigzagConversion('PAYPALISHIRING', 3)) # PAHNAPLSIIGYIR
	print(zigzagConversion('PAYPALISHIRING', 4)) # PINALSIGYAHRPI
	print(zigzagConversion('A', 1)) # A

#testZigzagConversion()

# Qustion 8: Convert a string to an integer taking any leading whitespace into account
# Make sure to account for +, - or integers that fall out of bounds potentially
'''
Must follow this algorithm:
1. Read in and ignore any leading whitespace.
2. Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
3. Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
5. If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
6. Return the integer as the final result.

00123
'''
def myAtoi(s):
	MIN = -2147483648 # Min bound for the integer that gets read in
	MAX = 2147483647 # Max bound for the integer that gets read in
	counter = 0 # Iterate throughout the string

	# Ignore all leading zeros
	while counter < len(s) and s[counter] == ' ':
		counter += 1

	# Case where we didn't find any relevant characters
	if counter == len(s):
		return 0

	val, firstVal = s[counter], s[counter] # Get first character, and build the numerical value of remaining characters
	#print('val so far:', val)
	counter += 1
	if not (firstVal.isdigit() or firstVal == '+' or firstVal == '-'):
		return 0 # First value isn't relevant? Return 0
	else:
		while counter < len(s) and s[counter].isdigit():
			val += s[counter] # Build the numerical value--note: stored backward
			counter += 1 # Increment the counter
		#print('val constructed: ', val, 'lenval:', len(val))
		num = 0
		if firstVal.isdigit(): # If the leading character is a digit
			num = int(firstVal) # Incorporate that digit into the actual final integer
		counter = 1
		for i in range(1, len(val)): # Iterate throughout the constructed string
			#print(i)
			num = num * 10 + int(val[i]) # Build the actual value
			#print('num, val:', num, val)

		if firstVal == '-': # Convert to a negative number
			num = -1 * num

	if num < MIN: # Check the lower bound
		return MIN # Return MIN value if less than lower bound
	elif num > MAX: # Check upper bound
		return MAX # Default to MAX value if greater than upper bound
	else:
		return num # Otherwise just return the ordinary number

def testMyAtoi():
	print(myAtoi('42')) # 42
	print(myAtoi('-42')) # -42
	print(myAtoi('   42')) # 42
	print(myAtoi('  -42')) # -42
	print(myAtoi("-91283472332")) # -2147483648 b/c exceeds lower bound
	print(myAtoi(' -42  trailing is fine')) # -42
	print(myAtoi('words then -42')) # 0--doesn't have leading whitespace


#testMyAtoi()

# Question 9: Check if Integer is a palindrome

# Memory inefficient, time efficient solution
def intPalindrome(x):
	stringX = str(x) # Convert integer to a string
	return stringX == stringX[::-1] and stringX.isdigit() # Make sure string reversed is the same and all characters are a digit

# What if we wanted to avoid converting to a string altogether?
'''
Ideas
- We need to extract one digit at a time: could we use recursion?
- Better idea: construct the reversed version of the integer w/o string operations
123321

'''
def intPalindrome(x):
	if x < 0: # Deal with base case of number < 0
		return False
	else:
		xCopy = x
		reversedX = 0
		while x > 0:
			reversedX = reversedX * 10 + x % 10
			x //= 10
		return xCopy == reversedX


'''
Question 10

Given an input string (s) and a pattern (p), implement regular expression matching with support 
for '.' and '*' where: 

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
'''

'''
Input/Output
'aa', 'a' --> false
'aa', 'a*' --> true
'ab', '.*' --> true
'aab', 'c*a*b' --> true
'mississippi', 'mis*is*p*.' --. false
'''


'''
Ideas
- Can take a recursive approach to this problem
	- Need to break down into 3 cases: 1. A character isn't followed by a *, 2. character is followed by *
	  but matches once, 3. Followed by * but we can match as many times as we'd like
	- Once the string is empty and pattern is empty, we know we've found a complete match
	- Otherwise, if the string (non-pattern version) isn't empty, this means that we didn't manage to find a match
		- Separating into these cases allows us to "skip" over the instances of *

Runtime/Memory analysis of this problem
- Allow S, P to represent the length of each string
- Worst case scenario occurs when we use the second case: followed by a *
	- Each time we encounter that case for a given part of the text, s[i:], p[2j:]
	  we construct strings of size S-i and P-2j
	  - There are (i+j choose i) ways of making this initial call to match(s[i:], p[2j:])
	    b/c we may have previously attempting to match the same pattern for a larger string
	    - We can see there is a way to improve this through dynamic programming to avoid repeat computation
- We need to sum over all possible lengths of s in each call and half the length of the pattern, P,
  since the worst case is populated entirely with *'s
- Overall runtime: sum_S(sum_P/2((i + j choose i) * O([S - i] + [P - 2j])))

'''

def isMatch(s, p): # s is the string, p is the pattern to match
	if not p: # If pattern is empty (we've gone through the entire pattern string)
		return not s # Return true IFF s is empty as well
	# Check to make sure our string still has characters to be matched AND a match can be made
	firstMatch = (s and (p[0] == '.' or p[0] == s[0]))
	# Case 1: our pattern is followed by a *
	if len(p) >= 2 and p[1] == '*':
		return ((firstMatch and isMatch(s[1:], p) or # Assume we found a match and want to use the same pattern
		(isMatch(s, p[2:])))) # Whether or not there was a match this time, we want to use the next pattern value
	else: # Case 2: our pattern isn't followed by a * so we just need to match a single character
		return firstMatch and isMatch(s[1:], p[1:]) # Make sure firstMatch is met + recurse through remainder of the strings

# Approach 2: dynamic programming
def isMatch2(s, p):
	memo = {} # Track if s[i:] matches pattern p[j:] using (i, j) as the key
	def helper(i, j): # Helper method that returns whether there's a match for s[i:], p[j:]
		if (i, j) not in memo: # We haven't encountered s[i:], p[j:]
			if j == len(p): # We have reached the end of pattern
				ans = (i == len(s)) # We have reached the end of the original string
			else:
				firstMatch = (i < len(s)) and (p[j] == s[i] or p[j] == '.') # Case 1: followed by 
				if j + 1 < len(p) and p[j+1] == '*': # Reached the case where we're followed by a *
					ans = (helper(i, j+2)  # Whether or not we found a match, move to next pattern
						or (firstMatch and helper(i+1, j))) # Found a match, use the same pattern against same string
				else: # Not followed by a *
					ans = firstMatch and helper(i+1, j+1) # Move onto next character in pattern and original string
			memo[i, j] = ans # Save the results in memo (memoization technique)
		return memo[i, j]
		# else: # We cached the results
		# 	return memo[(i, j)] # Return the result stored in memoized dictionary
	return helper(0, 0)
def testMatching():
	print(isMatch('aa', 'a')) # false
	print(isMatch('aa', 'a*')) # true
	print(isMatch('ab', '.*')) # true
	print(isMatch('aab', 'c*a*b')) # true
	print(isMatch('mississippi', 'mis*is*p*.')) # false

#testMatching()

def testMatching2():
	print(isMatch2('aa', 'a')) # false
	print(isMatch2('aa', 'a*')) # true
	print(isMatch2('ab', '.*')) # true
	print(isMatch2('aab', 'c*a*b')) # true
	print(isMatch2('mississippi', 'mis*is*p*.')) # false
#testMatching2()

