# import math

# def factorial(n):
#     return(math.factorial(n))

# #drives code
# num = 5
# print("factorial of",num,"is",
# factorial(num))


# #################################
# import math
# def factorial(n):
#     return(math.factorial(n))

# #drivers code
# num = 8
# print("factorial of",num,"is",
# factorial(num))




def factorial(n):

    return 1 if(n ==1 or n==0)else n*factorial(n-1)

num = 1
print("factorial is ",num,"is",factorial(num))


def factorial(n):

#condition
    return 1 if (n==1 or n==0)else n*factorial(n-1)
num = 6
print("factorail is ",num,"is",factorial(num))