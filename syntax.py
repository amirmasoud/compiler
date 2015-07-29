
class inclusiveRange():

	def function():
		pass

	def __init__(self, *args):
		count = len(args)
		if count < 1 :
			raise TypeError("Enter at least one number idiot! :P")
		elif count == 1:
			self.end = args[0]
			self.start = 0
			self.step = 1
		elif count == 2:
			(self.start, self.end) = args
			self.step = 1
		elif count == 3:
			(self.start, self.end, self.step) = args
		else:
			raise TypeError("3 Character at most but you entered {}, can you understand that?".format(count))

	# make object an iterable object
	def __iter__(self):
		i = self.start
		while i <= self.end:
			yield i
			i += self.step
def main():
	ir = inclusiveRange(10)
	for i in ir:
		print(i, end = "")

if __name__ == "__main__" : main()