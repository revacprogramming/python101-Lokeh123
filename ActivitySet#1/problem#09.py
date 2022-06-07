# fname = input("Enter file name: ")
fh = open(fname)
lst = list()                       
for lin e in fh:                    
    word= line.split()    
    for elem e nt in word:             
        if element in lst:         
            continue              
        else :                     
            lst.append(element)        
lst.sort()                        
print(lst)