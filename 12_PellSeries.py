pell=[0,1]
for i in range(2,20):
    pell.append(2*pell[-1]+pell[-2])
print(*pell)
# Here in the print we use *pell because we want output as series not list.
# If we print pell the output is in list


# FIbonacci series using list
f=[0,1]
for i in range(2,20):
    f.append(f[-1]+f[-2])
print(*f)


# Pell Series using logic
n=int(input())
a,b=0,1
count=0
while count<n:
    print(a,end=" ")
    a,b=b,2*b+a
    count+=1
