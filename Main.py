n=int(input("Enter N"))
x=int(input("Enter X"))
y=int(input("Enter Y"))
t=int(input("Enter T"))
listA=[]
listB=[]

for i in range(x,n+1,x):
    listA.append(i)
for i in range(y,n+1,y):
    listB.append(i)
 
    
print("************* List A is ************")
print(listA)

print("************* List B is ************")
print(listB)

print("************ Pairs are whose sum equals to T **************")
for i in listA:
    k=t-i
    if(k in listB):
        print(i,k)
        
    
