name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts=dict()
for line in handle:
    if not line.startswith("From:"):
        continue
    words=line.split()
    y=(words[1:])
    for word in y:
        counts[word]=counts.get(word,0)+1
 
    largestcount = 0
    largestword =0
    for word,count in counts.items():
        if largestcount is 0 or count > largestcount:
           largestword=word
           largestcount=count
print(largestword,largestcount)