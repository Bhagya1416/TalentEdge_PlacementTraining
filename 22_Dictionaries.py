#22-09-2026
msg="hihello saroja bagunnara bye"
freq={}
for i in msg:
    freq[i]=freq.setdefault(i,0)+1
print(freq)
#if we want key value 
for k,v in freq.items():
    print(k,v)
