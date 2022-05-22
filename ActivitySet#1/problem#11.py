name = raw_input("Enter file:")
handle = open(name)
d=dict()
for line in handle:
    if not line.startswith("From "): 
        continue
    else:    
        a=line.split()
        x=a[5]
        y=x[0:2]
        d[y]=d.get(y,0)+1

lst=list()        
for value,count in d.items():
    lst.append((value,count))

lst.sort()
for value,count in lst:
    print (value,count)