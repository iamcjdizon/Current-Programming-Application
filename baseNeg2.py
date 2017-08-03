def toBaseNeg2(d):
	a=""
	while(d!=0):
		rem = d % -2
		d = math.ceil(d/-2)
		a = str(int(math.fabs(rem))) + a
	return(a)

def toDeci(d):
	bla = d[::-1]
    sum = 0
    for i in range(len(d)):
        if i%2:
            sum += int(bla[i]) * -2**i
        else:
            sum += int(bla[i]) * 2**i
    return sum

import math
#deci = int(input("Enter a decimal number: "))
#print(toBaseNeg2(deci))
bin = input("Enter number: ")
print (toDeci(bin))