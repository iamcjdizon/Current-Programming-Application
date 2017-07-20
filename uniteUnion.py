def unite(*list1):
    list2 = []
    for l in list1:
        for i in l:
        	if not (('[' in i) or (']' in i) or (',' in i)):
           		if not i in list2:
           			list2.append(i)

    print(list2)

list1 = input("Input: ")
unite (list1)
#unite ([],[1,5,3],[1,2],[3,4,1])