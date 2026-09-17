'''
Amicable numbers are two different numbers where:
The sum of the proper divisors of the first number = the second number,
and the sum of the proper divisors of the second number = the first number.
'''
def sum_of_proper(n):
    total=0
    for i in range(1,n):
        if n%i==0:
            total+=i
    return total
def is_amicable(x,y):
    if x==y:
        return False
    else:
        return sum_of_proper(x)==y and sum_of_proper(y)==x
x=int(input())
y=int(input())
print("Output","Yes" if sum_of_proper(x)==y and sum_of_proper(y)==x else "No")