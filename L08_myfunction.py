# name="my name is NSN"
# print(name.title())
# print(name.lower())
# print(name.upper())
# print(name.isupper())
# print(name.islower())
# print(name.isdigit())
# print(name.split(" "))
#
# ans = name.split(" ")
# print(ans)
# print(name.capitalize())
#
# def mysum(x,y):
#     return x+y
#
# def maxnum(x,y):
#     if x>y:return x
#     else: return y
#
#
# a,b,c = int(input("Enter a number : ")), int(input("Enter a number : ")), int(input("Enter a number : "))
# print(mysum(a,b))
# print("Max number is : ",maxnum(a,maxnum(b,c)))

#
# n = int(input("Enter a number for fac: "))
# def myfact(x):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
#
# def myfact1(y):
#     if n==1:
#         return n
#     else:
#         return y*myfact1(y-1)
#
# print(myfact1(n))
#
# name = input("Enter a name : ")
#
# def check(name):
#     if(name==name[::-1]):
#         print("Name is palindrome")
#     else:
#         print("Name is not palindrome")
#
# check(name)

# ===================== SWAP TWO NUMBER ===================

# a,b,c = int(input("Enter value of a: ")), int(input("Enter value of b: ")), int(input("Enter value of c: "))

#
# def swap(x,y,z):
#     return(z,y,x)
#
# print(swap(a,b,c))

# def myswap():
#     global a,b,c
#     a,b,c=c,b,a
#     print("Inside funtion: ",a,b,c)
#
# myswap()
# print("Outside function: ", a,b,c)

def myswap(mylist):
    mylist[0],mylist[1]=mylist[1],mylist[0]
    print(mylist)

mylist = [10,20]
myswap(mylist)
print(mylist)