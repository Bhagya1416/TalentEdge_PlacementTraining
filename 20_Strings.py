# 16-09-2026
# Basic concepts of strings
''' 
Strings are immutable, the original string cannot be replaced or modified.
count(),len()
split()-consider spaces by default. This method is most efficient.
join()-used to combine elements. List of string words are only join using join() method.
These two are most important methods in strings.
isalpha()-checks all characters are alphabets are not.
isalnum()-checks whether all characters are either numbers or alphabets.
isdigit()-checks only digits.
strip()-to remove extra spaces.
lstrip()-to remove left spaces.
rstrip()-to remove right spaces.
replace() uses search method.
find()-finds the word.
find() and index() are used for almost same purpose.

>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

>>> help(str.join)
Help on method descriptor join:
join(self, iterable, /) unbound builtins.str method
    Concatenate any number of strings.
    The string whose method is called is inserted in between each given string.
    The result is returned as a new string.
    Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'

'''

# 1.How many vowels and consonants
a="BhagyaLakshmi" #this logic will work only for no space input
v=0
c=0
vo=['a','e','i','o','u']
for i in a:
    if i in vo:
        v+=1
    else:
        c+=1
print(v,c)


# 2.How many words in the string
msg="Hi, How are you?"
v=0
for i in msg:
    if i==" ":
        v+=1
print(v+1)
#print(len(msg.split()))


# 3.Reverse each word
msg="Hi, How are you?"
d=msg.split()
print(d)
l=[]
for i in d:
    l.append(i[::-1])
print(' '.join(l))


# 4.Find length of each word
msg="Hi, How are you?"
v=1
for i in msg.split():
    print(v,i,len(i))
    v+=1


# 5.Remove duplicates
msg="rajaassab"
res=''
for i in msg:
    if i not in res:
        res+=i
print(res)




    