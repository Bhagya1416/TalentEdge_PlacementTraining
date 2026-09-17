# Sum of the digits == Products of the digit
n=int(input())
sum=0
product=1
while n>0:
    digit=n%10
    sum+=digit
    product*=digit
    n//=10
if sum==product:
    print("Spy")
else:
    print("No")


# 1124 is a Spy Number