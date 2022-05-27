def computepay(h, r):
    if h>40 :
        a = h*r + (h-40)*(r*1.5) 
    else :
        a = h*r
	return a        
        
hrs = input ("Enter Hours:")
h=float(hrs)
rate = input("enter rate:")
r= float(rate)
pay = computepay(h, r)
print("Pay",pay)