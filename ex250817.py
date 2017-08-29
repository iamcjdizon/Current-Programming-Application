class Fraction:
		
	def __init__(self, numerator, denominator):
		self.numerator = numerator
		self.denominator = denominator
	
	def gcd(self, num1, num2):
		temp = 0;
		while num1>0:
			temp = num1
			num1 = num2 % num1
			num2 = temp
		return num2

	def simplify(self):
		bla = self.gcd(self.numerator, self.denominator)
		self.numerator = self.numerator / bla
		self.denominator = self.denominator / bla
		if(self.numerator!=self.denominator):
			return str(self.numerator) + "/" + str(self.denominator)
		else:
			return 1

	def liitan(self, num, den):
		bla = self.gcd(num, den)
		num = num / bla
		den = den / bla
		if(num!=den):
			return str(num) + "/" + str(den)
		else:
			return 1

	def __str__(self):
		return str(self.numerator) + "/" + str(self.denominator)

	def __add__(self, other):
		if other.denominator == self.denominator:
			return self.liitan(self.numerator+other.numerator, self.denominator)
		else:
			bla = self.gcd(self.denominator, other.denominator)
			return self.liitan((bla/self.denominator*self.numerator) + (bla/other.denominator*other.numerator),bla)

	def __sub__ (self, other):
		if other.denominator == self.denominator:
			return 	str(self.numerator-other.numerator) + "/" + str(self.denominator)
		else:
			bla = self.gcd(self.denominator, other.denominator)
			return str((bla/self.denominator*self.numerator) - (bla/other.denominator*other.numerator)) + "/" + str(bla)

	def __mul__ (self, other):
		 return self.liitan(self.numerator*other.numerator, self.denominator*other.denominator)


	def __truediv__ (self, other):
		return self.liitan(self.numerator*other.denominator, self.denominator*other.numerator)

class Polygon:

	noSides = 0
	length = []
	def __init__(self, noSides, *length):
		self.noSides = noSides
		self.length = length
	
	def perimeter(self):
		return sum(self.length)

 
class Quadrilateral(Polygon):

	def displayKind(self):
		if(self.noSides == 4):
			if(sum(self.length)/4 == self.length[0]):
				return "square"
			elif(self.length[0]==self.length[2] or self.length[1]==self.length[3])
				return "rectangle"
			elif(self.length[0]==self.length[1] or self.length[2]==self.length[3])
				return "kites"

		else:
			return "others"