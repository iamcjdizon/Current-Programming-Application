def matrices(M):
	n = len(M)-1
	ctr = 0
	sum = 0
	product = 1
	column = n
	row = 0
	while ctr<=n*2:
		if ctr==0:
			product = product * M[row][column]	

		elif ctr<=n:
			row = ctr
			column = n
			while row>-1:
				product = product * M[row][column]	
				if row>-1:	
					row-=1
					column-=1
				else:
					break

		elif ctr>n:
			row = n
			column = n - (ctr-n)
			while (row!=0 or column!=0):
				product = product * M[row][column]
				if column!=0:	
					row-=1
					column-=1
				else:
					break


		sum = sum + product
		product = 1
		ctr+=1

	ctr2 = 0
	sum2 = 0
	product2 = 1
	column2 = 0
	row2 = 0
	while ctr2<=n*2:
		if ctr2==0:
			product2 = product2 * M[row2][column2]	

		elif ctr2<=n:
			row2 = ctr2
			column2 = 0
			while (row2!=-1):
				product2 = product2 * M[row2][column2]	
				if row2!=-1:	
					row2-=1
					column2+=1

		elif ctr2>n:
			row2 = n
			column2 = ctr2-n
			while (row2!=0 or column2!=n):
				product2 = product2 * M[row2][column2]
				if column2!=n:	
					row2-=1
					column2+=1
				else:
					break

		sum2 = sum2 + product2
		product2 = 1
		ctr2+=1
	return (sum-sum2)

def blah(M):
	print(len(M))
	return 

#n = int(input ("Enter dimension of the square matrix: "))
#M=[]
#m=[]
#while (len(m)!=(n*n)):
#	m = list(map(int, input("Please input " + str(n*n) + " values which represents the whole matrix: ").split(",")))

#M = [m[i:i + n] for i in range(0, len(m), n)]
M = [[1,2,3],[4,5,6],[7,8,9]]
#print("Diagonal Products is: "+ str(matrices(M)))
#blah(M)
print(matrices(M))
#print(matrices2(n-1, M))
#print (M[0][1])