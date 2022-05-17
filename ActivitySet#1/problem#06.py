largest = None
smallest = None
while True:
    num = input ("Enter a number: ")
    if num == "done":
        break
    try:
        i=int(num)
        if largest is None:
            largest=i
        elif largest >i:
            largest =largest
        else:
            largest=i
        if smallest is None:
            smallest=i
        elif smallest<i:
            smallest=smallest
        else:
            smallest=i
    except:
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)