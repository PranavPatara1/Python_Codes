Lst1 = [i*i for i in range(1,41)]
Lst2 = []
a=0

for i in range (1, len(Lst1)):
    a =  Lst1[i] - Lst1[i-1]
    Lst2.append(a) 

print(Lst1)
print(Lst2)