#print cube of first n natural numbers
def sumofSeries(n):
    x = (n*(n+1)/2)
    return (int)(x*x)

n=5
print(sumofSeries(n))



n = int(input("enter the number"))
for i in range(n):
    print(i**2)