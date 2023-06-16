# a = ["Raj","Ram","Ramesh"]
#
# print(a)
#
# for i in range(len(a)):
#     print(a[i])
#
# for i in range(len(a)):
#     print(a[len(a)-1-i])    #reverse print
#
# for data in a:
#     print(data)
#
# print(type(a))
# print(id(a))    #self intro inspecsation
#
# list1 = [1,2,3,4,5,6,7,8,9,10]
# for i in range(len(list1)-1,-1,-1):
#     print(i,end=" !")
#
# ======================= DIC ===================================
#
# dict1 = {"Name":"NSN", "Roll_no.":"21ECOCS021"}
# print(dict1)
# for data in dict1.items():
#     print(data)
#
# for data in dict1.items():
#     print(data[0],data[1])
#
# for data in dict1.values():
#     print(data)
#
# for data in dict1:
#     print(dict1[data])
#
# print(dict1.items())
# print(dict1.values())
# import math
#
# list1 = ["Ram",1,"NSN",'A']
# print(list1)
# print(type(list1))
#
# list2=list1
# print(list2)
# list1.append("B")
# print(list1)
# list1.pop()
# print(list1)
# list1.insert(2,100)
# print(list1)
# del list1[1:2]
# print(list1)
#
# list3=[1,2,-3,4,-5,-6,0]
# pos=0
# neg=0
# zero=0
# for data in list3:
#     if(data>0):
#         pos+=1
#     elif(data<0):
#         neg+=1
#     else:
#         zero+=1
# print("Positives are : ",pos)
# print("Negatives are : ",neg)
# print("Zero are : ",zero)
#
# list = ["Mr. Ram","Miss Sita","mr. NSN"]
# boy=0
# girl=0
# for data in list:
#     if "Mr." in data.title():
#         boy+=1
#     else:
#         girl+=1
# print("Boys are : ", boy)
# print("Girls are : ", girl)

# a=[]
# n=int(input("How many elements you want to enter : "))
#
# for i in range(n):
#     a.append(int(input("Enter the element : ")))
# search = int(input("Enter the data you want to search: "))
#
# if search in a:
#     print("Yes found at postion: ", a.index(search)+1)
# else:
#     print("Not found")

# a=[]
# n=int(input("How many elements you want to enter : "))
#
# for i in range(n):
#     a.append(int(input("Enter the element : ")))
#
# for data in a:
#     fact = math.factorial(data)
#     print("factorial of ", data, "is : ",fact)

# for data in a:
#     fact = 1
#     for i in range(1,data+1):
#         fact=fact*i
#     print("factorial of ", data, "is : ",fact)
# def myfact(data):
#     if data == 1:
#         return data
#     else:
#         return data*myfact(data-1)
#
# for data in a:
#     myfact(data)
#     print(f"fact is : {data}")
# =====================================

# a={1,2,3,4}
# b={1,2,8,6}
# print(a|b)
# print(a&b)
# print(a-b)
# print(b-a)
# print(a.symmetric_difference(b))

