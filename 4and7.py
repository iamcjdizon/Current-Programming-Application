number = int(input("Enter number: "))
for i in range(4,number+1):
	if ((i % 4 ==0) and (i % 7 == 0 )):
		print (i, end = ' ');