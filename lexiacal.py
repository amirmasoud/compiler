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

	#available operands
	operator = (plus, minus, mul, div, lessThan, greaterThan, openPran, closePran, openBrac, closeBrac, openAcco, closeAcco, comma, semCol)

	#output file
	of = []

	# Start line number
	lineNumber = 1

	# Error output file
	lerr = open("errors.lerr", "w")

	# Symbol table file
	symTable = open("symTable.txt", "w")

	def __init__(self):
		self.readFile()

	#
	#	Read input.txt file
	#
	def readFile(self):

		# Start reading from input file
		infile = open("input.txt")
		for line in infile:

			# Read each line and specify each token
			self.s = line
			self.nextToken()
			self.lineNumber += 1

	#
	#	Lexiacl Analyzer
	#
	def nextToken(self):
		begin =  forward = 0

		# check end of the string
		while forward < len(self.s):

			# 
			# 	Skip white spaces
			# 
			if self.s[forward] == " ":
				begin = forward

			#
			#	IDs & Keywords
			#
			elif self.s[forward] in self.ll or self.s[forward] == "_":
				begin = forward
				while self.s[forward] in self.ll or self.s[forward] in self.nl or self.s[forward] == "_":
					forward += 1
				if self.s[begin:forward] in [x for x in self.keywords]:
					print(self.lineNumber, begin, "keyword", self.s[begin:forward])
					keywordToWrite = (self.lineNumber, begin, "keyword", self.s[begin:forward], "\n")
					self.symTable.write('	'.join('%s' % x for x in keywordToWrite))
				else:
					self.keywords.append((self.lineNumber, begin, self.s[begin:forward]))
					print(self.lineNumber, begin, "id", self.s[begin:forward])
					idToWrite = (self.lineNumber, begin, "id", self.s[begin:forward], "\n")
					self.symTable.write('	'.join('%s' % x for x in idToWrite))
				forward -= 1

			#
			#	Numbers
			#
			elif self.s[forward] in self.nl:
				begin = forward
				forward += 1
				while self.s[forward] in self.nl:
					forward += 1
					if forward >= len(self.s):
						break
				if self.s[forward] == ".":
					forward +=1
				while self.s[forward] in self.nl:
					forward += 1
					if forward >= len(self.s):
						break
				print(self.lineNumber, begin, self.s[begin:forward])
				digit = (self.lineNumber, begin, self.s[begin:forward], "\n")
				self.symTable.write('	'.join('%s' % x for x in digit))
				forward -= 1

			#
			#	:=/<=/>=/!=/==
			#
			elif self.s[forward] in (':', '<', '=', '!', '>'):
				begin = forward
				forward += 1
				try:
					if self.s[forward] == "=":
						forward += 1
						print(self.lineNumber, begin, self.s[begin:forward])
						op2Char = (self.lineNumber, begin, self.s[begin:forward], "\n")
						self.symTable.write('	'.join('%s' % x for x in op2Char))
				except:
					for op in self.operator:
						print(op)
					print(self.lineNumber, begin, self.s[forward-1])
					op2Char = (self.lineNumber, begin, self.s[forward-1], "\n")
					self.symTable.write('	'.join('%s' % x for x in op2Char))
				forward -= 1

			#
			#	Comments
			#
			elif self.s[forward] in [x[1] for x in self.operator]:
				begin = forward
				if self.s[forward] == '/':
					forward += 1
					if self.s[forward] == "*":
						forward += 1
						while self.s[forward] != '*':
							forward += 1
							if forward >= len(self.s):
								break
						forward += 1
						if self.s[forward] == '/':
							forward += 1
					else:
						forward -= 1
				else:
					for op in self.operator:
						if op[1] == self.s[forward]:
							print(self.lineNumber, begin, op[0])
							opToWrite = (self.lineNumber, begin, op[0], "\n")
							self.symTable.write('	'.join('%s' % x for x in opToWrite))


			#
			#	Errors
			#
			else:
				begin = forward
				print(self.lineNumber, begin, self.s[begin:forward],"undefinded charecter")
				error = (self.lineNumber, begin, self.s[begin:forward],"undefinded charecter", "\n")
				self.lerr.write('	'.join('%s' % x for x in error))
			forward += 1


		#
		#	Print all keywords + IDs
		#
		print(self.keywords)
def main():

	token()

# main Program
if __name__ == "__main__" : main()