n = int(input("Enter a number: "))
print ([i for i in range(n)])
print ([i*i for i in range(n)])
print ([i*i for i in range(-n+1,n)])
print ([i for i in range(1,n+1) if n%i==0])
print ([i*i for i in range(1,n+1) if n%i==0])