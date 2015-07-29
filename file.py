def main():
	infile = open("1.jpg", 'rb')
	outfile = open('new.jpg', 'wb')
	bufferSize = 50000
	buffer = infile.read(bufferSize)
	while len(buffer):
		outfile.write(buffer)
		print(".", end = '')
		buffer = infile.read(bufferSize)
	print("Done.")
if __name__ == "__main__" : main()