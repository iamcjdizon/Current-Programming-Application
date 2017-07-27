word = input(r"Enter a string: ")
d = {'LETTERS':0, 'DIGITS':0}
for i in word:
	if i.isdigit():
		d['DIGITS'] += 1
	elif i.isalpha():
		d['LETTERS'] +=1
print (d)