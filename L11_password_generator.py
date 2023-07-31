import random
#
# def function():
#     n = int(input("Enter the length of password: "))
#     password = ''
#     for i in range(n):
#         a=chr(random.randint(48,122))
#         if a not in password:
#             password+=a
#         else:
#             n+=1
#     print(password)
#
# function()
# ==============ANOTHER METHOD===========================================

import string

s1 = string.ascii_uppercase
print(s1)
s2 = string.ascii_lowercase
print(s2)
s3 = string.digits
print(s3)
s4 = string.punctuation
print(s4)

s = []
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)
print(s)

random.shuffle(s)

print(s)

n = int(input("Enter the length of password: "))
print("".join(s[0:n]))

print("".join(random.sample(s,n)))
