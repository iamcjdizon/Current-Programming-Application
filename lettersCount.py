word = input("Enter a word: ")
d = {}
for i in word:
	d[i] = word.count(i)
print (d)