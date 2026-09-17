# Properly Ordered means ascending or descending eg: 1379, 7521
def is_proper(n):
    digit=str(n)
    ascending=descending=True
    for i in range(len(digit)-1):
        if digit[i]<digit[i+1]:
            descending=False
        elif digit[i]>digit[i+1]:
            ascending=False 
    return ascending or descending
num=int(input())
print("Output: ","Yes" if is_proper(num) else "No")

