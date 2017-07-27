from functools import reduce

def vowelCount(bla):
	#vowelsCount=0
	for i in bla.read():
		#if ((i=='a') or (i=='e') or (i=='i') or (i=='o') or (i=='u')):
		vowelsCount = bla.read().count(i)
			#vowelsCount+=1	
	return vowelsCount


word = open("sample", "r")
L= vowelCount(word)
print(L)