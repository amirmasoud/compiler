#import regular expression library
import string

class token():

	# list of letters a-zA-Z
	ll = list(string.ascii_letters)

	#list of numbers 0-9
	nl = list(string.digits)


	# Reserved keywords
	intQ	 	= "int"
	doubleQ 	= "double"
	voidQ 		= "void"
	ifQ 		= "if"
	elseQ 		= "else"
	whileQ 		= "while"
	returnQ 	= "return"
	keywords = [intQ, doubleQ, voidQ, ifQ, elseQ, whileQ, returnQ]
	idIndex = []

	# Reserved operator
	plus 				= ("plus", "+")
	minus 				= ("minus", "-")
	mul 				= ("mul", "*")
	div 				= ("div", "/")
	lessThan 			= ("LessThan", "<")
	greaterThan 		= ("GreaterThan", ">")
	openPran 			= ("OpenPran", "(")
	closePran 			= ("ClosePran", ")")
	openBrac 			= ("OpenBrac", "(")
	closeBrac 			= ("CloseBrac", "]")
	openAcco 			= ("OpenAcco", "{")
	closeAcco 			= ("CloseAcco", "}")
	comma 				= ("Comma", ",")
	semCol 				= ("SemCol", ";")
	assign 				= ("assign", ":=")
	lessThanEqual 		= ("LessThanEqual", "<=")
	Equal 				= ("Equal", "==")
	notEqual 			= ("NotEqual", "!=")
	greaterThanEqual 	= ("GreaterThanEqual", ">=")
	commentStart		= ("CommentStart", "/*")
	commentEnd 			= ("CommentEnd", "*/")

	#available operands
	operator = (plus, minus, mul, div, assign, lessThan, lessThanEqual, Equal, notEqual, greaterThanEqual, greaterThan, openPran, closePran, openBrac, closeBrac, openAcco, closeAcco, comma, semCol, commentStart, commentEnd)
	opIndex = []
	#output file
	of = []
	def __init__(self, s):
		self.s = s
		self.nextToken()

	def nextToken(self):
		
		# string index
		i = 0

		# loop through the string
		# first phase: finding all operators
		while i < len(self.s):

			# 1 char operand
			char1 = self.s[i]

			# 2 chars operand := >= <= == != /* */
			try:
				char2 = self.s[i+1]
			except:
				char2 = ""

			for opName, opValue in self.operator:
				if opValue == char1 + char2:
					self.opIndex.append(i)
					self.opIndex.append(i+1)
					self.of.append((i, opName))
					i += 1
					print(i-1, i, opValue, opName)
			for opName, opValue in self.operator:
				if opValue == char1 and i not in self.opIndex:
					self.opIndex.append(i)
					self.of.append((i, opName))
					print(i, opValue, opName)
			i+=1
			
		# remove duplicated items
		# sort them and put it on the list
		missedIndex = []
		self.opIndex = sorted(set(self.opIndex))

		# find comment
		for ofi in self.of:
			commentStartIndex 	= None
			commentEndIndex 	= None
			if ofi[1] == 'commentStart':
				commentStartIndex = ofi[0]
				self.of.append((commentStartIndex, "CommentStart"))
			if ofi[1] == 'commentEnd':
				commentEndIndex = ofi[0]
				self.of.append((commentEndIndex, "CommentEnd"))


		# finding missed indices of string
		# these missed indices are id or number
		for oi in range(len(self.s)):
			if oi not in self.opIndex:
				missedIndex.append(oi)


		# seprate missed indices
		idStart = missedIndex[0]
		i = 0
		while i < (len(missedIndex) - 1):
			# last one
			if missedIndex[i+1] == missedIndex[-1]:
				self.of.append((idStart, "id"))
						

			# finding sequence numbers in list
			elif missedIndex[i+1] - missedIndex[i] > 1:

				# split them with space
				#ids = self.s[idStart:missedIndex[i]+1].split(" ")
				si = idStart
				while si < missedIndex[i] + 1:
					while self.s[si] == " ":
						si += 1
					#print(self.s[si + 1])
					si += 1
				#print(ids)
				idStart = missedIndex[i+1]
			i += 1
			#print(self.of)


def main():
	s = "{ int cnt == _var2c - 3.14342;/*it is*/"
	#print(len(s))
	token(s)

# main Prog
if __name__ == "__main__" : main()