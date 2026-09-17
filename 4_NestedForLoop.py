'''
for x in range(5):
    for y in range(5):
        print(x)

for x in range(5):
    for y in range(5):
        print(y)

for x in range(5):
    for y in range(5):
        print(x,y)

for x in range(5):
    print()
    for y in range(5):
        print(y)
'''
for x in range(5):
    print()
    for y in range(5):
        print("(",x,",",y,")",end=" ")
        
        # print(f"({x},{y})",end=" ")  
        # This is the best way to print the values of x and y in a single line.
        # The above line is called f-string formatting.
