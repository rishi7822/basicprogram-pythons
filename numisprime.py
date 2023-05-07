num = int(input("enter the number"))

if num > 1:
    #iterate from 2 to n/2
    for i in range(2,int(num/2)+1):
        #not divisble by 2 it isprime
        if (num %i)==0:
            print("num is not prime")
            break
    else:
            print("num isprime")
else:
        print("not prime")