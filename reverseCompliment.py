strand = input("Enter DNA Sequence: ")
dna = strand.upper()
rna = ''
for i in reversed (dna):
	if i == 'T':
		rna+='A'
	elif i == 'A':
		rna+='T'
	elif i == 'C':
		rna+='G'
	elif i == 'G':
		rna+='C'
	else:
		rna = 'Invalid'
		break
		
print (rna)
	