'''
Question 7: Easy
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x 
causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
'''
def reverseInt(x):
	temp = abs(x)
	reversedInt = 0
	while temp > 0:
		reversedInt = reversedInt * 10 + temp % 10
		temp = temp//10
	if reversedInt >= 2 ** 31 - 1:
		return 0
	elif x > 0:
		return reversedInt
	else:
		return -1 * reversedInt

def reverseIntTestCases():
	print(reverseInt(123))
	print(reverseInt(-123))
	print(reverseInt(120))
	print(reverseInt(1534236469))


''' 
190: Easy
Reverse the bits for a 32 bit unsigned integer 
'''
def reverseBits(n):
	# Works for a generic length
	reversedBits = 0
	for i in range(32):
		reversedBits += (n & 1)
		#print(reversedBits)
		if i != 31:
			reversedBits <<= 1
		n >>= 1
	return reversedBits

# Alternate Sol: Add the flipped bits in accordance to their position
def reverseBits1(n):
	val, exp = 0, 31
	while n > 0:
		val += (n & 1) << exp # Add the exp-th bit adjusted in accordance to bit position
		n >>= 1 # Integer divide by 2
		exp -= 1 # Decrement the bit position
	return val

def testReverseBits():
	print(reverseBits1(43261596))
	print(reverseBits1(4294967293))


'''
Question 13: Easy
Convert a roman numeral to an integer bounded by [1, 3999]
'''

def romanToInt(s):
	total = 0
	encodings = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
	total += encodings[s[0]] # Add the initial value
	for i in range(1, len(s)):
		total += encodings[s[i]] # Add the encoded current value
		if encodings[s[i]] > encodings[s[i-1]]: # If the previous value was larger --> we need to subtract off
			total -= 2 * encodings[s[i-1]]
	return total


def testRomanToInt():
	print(romanToInt('III')) # 3
	print(romanToInt('IV')) # 4
	print(romanToInt('IX')) # 9
	print(romanToInt('LVIII')) # 58
	print(romanToInt('MCMXCIV')) # 1994

'''
12: Medium
Convert integer to roman numeral, bounded by: [1, 3999]
'''

def intToRoman(num):
	roman = ''
	encodings = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), 
	('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]
	counter = 0
	while num > 0:
		if num < encodings[counter][1]:
			counter += 1
		else:
			roman += encodings[counter][0]
			num -= encodings[counter][1]
	return roman




print(intToRoman(3)) # 'III'
print(intToRoman(4)) # 'IV'
print(intToRoman(9)) # 'IX'
print(intToRoman(58)) # 'LVIII'
print(intToRoman(1994)) # 'MCMXCIV'


















