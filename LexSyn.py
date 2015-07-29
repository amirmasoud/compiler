import string

class compiler():

	# list of letters a-zA-Z
	ll = list(string.ascii_letters)

	#list of numbers 0-9
	nl = list(string.digits)


	# Reserved keywords
	intQ		= "int"
	doubleQ 	= "double"
	voidQ 		= "void"
	ifQ 		= "if"
	elseQ 		= "else"
	whileQ 		= "while"
	returnQ 	= "return"
	keywords = [intQ, doubleQ, voidQ, ifQ, elseQ, whileQ, returnQ]
	idIndex = []

	# Reserved operator
	# plus 				= ("plus", "+")
	# minus 				= ("minus", "-")
	# mul 				= ("mul", "*")
	# div 				= ("div", "/")
	# lessThan 			= ("LessThan", "<")
	# greaterThan 		= ("GreaterThan", ">")
	# openPran 			= ("OpenPran", "(")
	# closePran 			= ("ClosePran", ")")
	# openBrac 			= ("OpenBrac", "(")
	# closeBrac 			= ("CloseBrac", "]")
	# openAcco 			= ("OpenAcco", "{")
	# closeAcco 			= ("CloseAcco", "}")
	# comma 				= ("Comma", ",")
	# semCol 				= ("SemCol", ";")


	plus 				= ("+", "+")
	minus 				= ("-", "-")
	mul 				= ("*", "*")
	div 				= ("/", "/")
	lessThan 			= ("<", "<")
	greaterThan 		= (">", ">")
	openPran 			= ("(", "(")
	closePran 			= (")", ")")
	openBrac 			= ("[", "[")
	closeBrac 			= ("]", "]")
	openAcco 			= ("{", "{")
	closeAcco 			= ("}", "}")
	comma 				= (",", ",")
	semCol 				= (";", ";")

	#available operands
	operator = (plus, minus, mul, div, lessThan, greaterThan, openPran, closePran, openBrac, closeBrac, openAcco, closeAcco, comma, semCol)

	# LL(1)
	# A Goes to end by A
	A = {'end': 'A', 'int': 'B A', 'bool': 'B A', 'void': 'B A', 'double': 'B A', '$': 'SYNC'}
	B = {'int': 'C', 'int': 'D', 'bool': 'C', 'bool': 'D', 'void': 'C', 'void': 'D', 'double': 'C', 'double': 'D', '$': 'SYNC'}
	C = {'int': 'E id F', 'bool': 'E id F', 'void': 'E id F', 'double': 'E id F', '$': 'SYNC'}
	D = {'int': 'E id F G', 'bool': 'E id F G', 'void': 'E id F G', 'double': 'E id F G', '$': 'SYNC'}
	E = {'int': 'int', 'bool': 'bool', 'void': 'void', 'double': 'double', 'id': 'SYNC'}
	F = {'(': '( )', '(': '( H I )', '$': 'SYNC', '{': 'SYNC'}
	G = {'{': '{ K }', '$': 'SYNC'}
	H = {'int': 'E id', 'bool': 'E id', 'void': 'E id', 'double': 'E id', ')': 'SYNC'}
	I = {',': ', H I', ')': '3'}
	J = {'(': '( )', '(': '( O W )'}
	K = {'id': 'L K', 'for': 'L K', 'if': 'L K', 'return': 'L K', '{': 'L K', '}': '3'}
	L = {'id': 'M ;', 'for': 'N', 'if': 'N', 'return': 'N', '{': 'G', '}': 'SYNC'}
	M = {'id': 'id := O', ';': 'SYNC', ')': 'SYNC'}
	N = {'for': 'for ( P ; O ; p ) L', 'if': 'if ( S ) L Q', 'return': 'return O ;', 'return': 'return ;', '}': 'SYNC'}
	O = {'(': 'U', 'number': 'U', 'true': 'U', 'false': 'U', ';': 'SYNC', '>=': 'SYNC', '<=': 'SYNC', '>': 'SYNC', '<': 'SYNC', '==': 'SYNC', '!=': 'SYNC', ')': 'SYNC', '(': 'SYNC', 'id': 'SYNC'}
	P = {'id': 'M', ';': '3', ')': '3'} 
	Q = {'else': 'else L', '}': 'SYNC'}
	S = {'!': '! O', '(': 'O T O', '(': 'O', 'id': 'O T O', 'id': 'O', 'number': 'O T O', 'number': 'O', 'true': 'O T O', 'true': 'O', 'false': 'O T O', 'false': 'O', ')': 'SYNC'}
	T = {'=>': '=>', '<=': '<=', '>': '>', '<': '<', '==': '==', '!=': '!=', '(': 'SYNC', 'num': 'SYNC', 'true': '=>', 'false': '=>'}
	U = {'(': 'V', 'id': 'V', 'number': 'V', 'true': 'V', 'false': 'V', '*': 'SYNC', '/': 'SYNC', ';': 'SYNC','=>': 'SYNC', '<=': 'SYNC', '>': 'SYNC', '<': 'SYNC', '==': 'SYNC', '!=': 'SYNC', ')': 'SYNC'}
	V =	{'(': '( O )', 'id': 'id', 'number': 'number', 'true': 'true', 'false': 'false', '*': 'SYNC', '/': 'SYNC', ';': 'SYNC', '=>': 'SYNC', '<=': 'SYNC', '>': 'SYNC', '<': 'SYNC', '==': 'SYNC', '!=': 'SYNC', ')': 'SYNC'}
	W = {',': ', O W', ')': '3'}

	grammer = (A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, S, T, U, V, W)

	stack = ['$', 'A']
	input = []
	output = []

	terminal = ('int', 'double', 'end')


	#output file
	of = []

	# Start line number
	lineNumber = 1

	# Error output file
	lerr = open("errors.lerr", "w")

	# Symbol table file
	symTable = open("symTable.txt", "w")

	lexiaclList = []

	def __init__(self):
		pass

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
			if self.s[forward] == " " or self.s[forward] == "\n" or self.s[forward] == "\t" or self.s[forward] == "\s":
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
					self.lexiaclList.append(self.s[begin:forward])
				else:
					self.keywords.append((self.lineNumber, begin, self.s[begin:forward]))
					print(self.lineNumber, begin, "id", self.s[begin:forward])
					idToWrite = (self.lineNumber, begin, "id", self.s[begin:forward], "\n")
					self.symTable.write('	'.join('%s' % x for x in idToWrite))
					self.lexiaclList.append('id')
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
				# self.s[begin:forward]
				digit = (self.lineNumber, begin, 'number', "\n")
				self.symTable.write('	'.join('%s' % x for x in digit))
				self.lexiaclList.append('number')
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
						self.lexiaclList.append(self.s[begin:forward])
						op2Char = (self.lineNumber, begin, self.s[begin:forward], "\n")
						self.symTable.write('	'.join('%s' % x for x in op2Char))
				except:
					for op in self.operator:
						print(op)
					print(self.lineNumber, begin, self.s[forward-1])
					op2Char = (self.lineNumber, begin, self.s[forward-1], "\n")
					self.lexiaclList.append(op2Char)
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
							self.lexiaclList.append(op[0])
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


	def first_set(self):
		print(type(self.grammer))
		for row in self.grammer:
			print(row)
		#print(self.grammer)

	def readLL1(self):
		returnValue = ()
		currentStack = self.stack[-1]
		selfProperty = getattr(self, currentStack)
		for values in selfProperty:
			for key in values:
				if(key == self.input[-1]):
					returnValue = values[-1]
					returnValue = returnValue.split(' ')
					returnValue = returnValue[::-1]
					return returnValue

	'''
		Loop through LL1 table 
		that made earlier
	'''
	def LL1(self):
		goesTo = []
		try:
			getProperty = getattr(self, self.stack[-1])
			goesTo = getProperty[self.input[-1]].split(' ')[::-1]

		# Error
		except KeyError:
			self.input.pop()
			return 'Not Found: key Error'

		# Error
		except AttributeError:
			self.input.pop()
			return 'Not Found: Attribute Error'

		# Found Something
		self.stack.pop()
		self.stack.extend(goesTo)

		# Correct search
		if self.stack[-1] == self.input[-1]:
			self.stack.pop()
			self.input.pop()
			return 'matched'

		# Panic Mode - Pop from stack
		elif self.stack[-1] == 'SYNC':
			self.stack.pop()
			return 'Panic Mod Sync'

		# Error
		elif goesTo != self.input[-1] and self.input[-1] in self.terminal and self.stack[-1] in self.terminal:
			self.stack.pop()
			return 'two not equal terminal'

	'''
		Debug stack, input, output stacks
	'''
	def debug(self):
		print('Stack:  ', self.stack)
		print('Input:  ', self.input)
		print('Output: ', self.output)


	'''
		Main Function for syntax Analyzer
	'''
	def syntax(self):
		self.lexiaclList.extend(['$'])
		self.lexiaclList.reverse()
		self.input = self.lexiaclList
		

		while self.input[-1] != '$':
		 	self.debug()
		 	print(self.LL1())
		self.debug()

		if len(self.stack) == 0 and len(self.input):
			print('    /                                  / ')
			print(' \ /  Correct: Successfuly parsed.  \ /  ')
			print('  ^                                  ^   ')

		else:
			print(' \ /                            \ / ')
			print('  X  Wrong: Failed to parse it.  X  ')
			print(' / \                            / \ ')

		#print(self.lexiaclList)




def main():

	lexiacl = compiler()
	lexiacl.readFile()

	syntax = compiler()
	syntax.syntax()

# main Program
if __name__ == "__main__" : main()