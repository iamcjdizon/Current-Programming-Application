limit = int(input("Enter limit of the sequence: "))
x=1; y=0
while x <= limit:
	x = x + y
	y = y + x
	if x<=limit:
		print (x, end=" ")
	if y<=limit:
		print (y, end=" ") 