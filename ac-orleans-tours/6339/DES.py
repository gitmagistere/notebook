from random import*
Liste1=[]
for i in range (0,30):
    a=randint(1,6)
    b=randint(1,6)
    print(a,b,a+b)
    Liste1.append(a+b)
print("Nb de fois 2 :",Liste1.count(2))