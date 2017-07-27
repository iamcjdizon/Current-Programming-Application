sample = [12, 24, 35, 70, 88, 120, 155]
A = [sample[y] for y in range(0, len(sample)) if y%2==1]
print (A)