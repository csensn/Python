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

dict1 = {"Name":"NSN", "Roll_no.":"21ECOCS021"}

for data in dict1.items():
    print(data)

for data in dict1.values():
    print(data)

for data in dict1:
    print(dict1[data])

print(dict1.items())
print(dict1.values())