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
# n = int(input("Enter a number for factorial : "))
# def myfact(x):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
#
# def myfact1(y):
#     if y==1:
#         return y
#     else:
#         return y*myfact1(y-1)
#

from L09_recursivefunction import *

myfact1(5)

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
#
# ===================== SWAP TWO NUMBER ===================
#
# a,b,c = int(input("Enter value of a: ")), int(input("Enter value of b: ")), int(input("Enter value of c: "))
#
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

# def myswap(mylist):
#     mylist[0],mylist[1]=mylist[1],mylist[0]
#     print(mylist)
#
# mylist = [10,20]
# myswap(mylist)
# print(mylist)

# def resume(name,fname, mclass):
#     print(f"""Hello {name}
#             father name is : {fname}
#             Class is : {mclass}""")
#
# resume("NSN","xyz","btech")
# resume("NSN2","xyz2","btech")
# resume("NSN3","xyz3",12)

# def update(list1):
#     for i in range(5):
#         list1[i]+=10
#     print(list1)
#
# list1=[1,2,3,4,5]
# update(list1)
# print(list1)

# def resume(name, roll):
#      print(f"Nme is {name} and roll no is {roll}")
# def resume(name="NSN", roll=23):        #default argument
#      print(f"Nme is {name} and roll no is {roll}")
#
# resume()
# resume("NSN2", 34)
# resume(roll=123,name="NSN")

# ============ VARIABLE LENGTH ARGUMENT==============
#
# def mysum(*a):
#     print(sum(a))
#     print(min(a))
#     print(max(a))
#     print(len(a))
#
# mysum(1,2,3)
# mysum(1,3)
# mysum(1,25,6,7,4,3)
# mysum(1,2,3,1)

#
# a=100   #global variable
#
# def show():
#     global a
    # x=globals()['a']
    # a=200
    # print(a)
    # print(x)
    # globals()['a']=300
    # a=400
    # print(a)
    # print(x)
#
# show()
# print(a)