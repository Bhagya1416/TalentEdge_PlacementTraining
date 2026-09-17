'''
A Disarium number is a number where the sum of its digits raised to the power of their respective positions equals the original number.
Positions start from 1 from the left.
Example: 135

Digits and positions:
1 → position 1
3 → position 2
5 → position 3

Calculate:
1¹ + 3² + 5³
= 1 + 9 + 125
= 135
'''

# enumerate gives the index/position, the value of that index/position
def is_disarium(n):
    digits=str(n)
    total=sum(int(d)**(i+1) for i,d in enumerate(digits)) # i=index, d=value
    return total==n
num=int(input())
print("Output:","Yes" if is_disarium(num) else "No")

