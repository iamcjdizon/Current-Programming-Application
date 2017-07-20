word = 'bla'
sampleList=[]
while word != 'stop':
	word = input("Enter a string: ")
	if len(word) < 3:
		print (word)
	elif ((len(word) >= 3) and (word != 'stop')):
		if word.endswith('ing'):
			print (word + "ly")
		else:
			print (word + "ing")
print ("Goodbye")