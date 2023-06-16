n = int(input("Enter a number for factorial : "))
def myfact1(y):
    if y==1:
        return y
    else:
        return y*myfact1(y-1)

print(myfact1(n))