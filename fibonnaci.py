a = int(input("enter the number:"))

f = 0 #first number
s = 1 #second number
#condition
if a<=0:
    print("requested series is\n",f)
else:
    print(f,s,end=" ")
    for x in range(2,a):
        next = f+s
        print(next,end = " ")
        f=s
        s=next
