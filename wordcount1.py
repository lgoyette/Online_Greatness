
def main():
	userWords = input("Enter a bunch of words:")
	wordCount = 0
	for i in userWords.split():
		wordCount += 1
	print("You entered " + wordCount + " words.")
if __name__ == '__main__':
  main()
