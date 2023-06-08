# Add two Numbers

# a = int(input("Enter a vulue of a: "))
# b = int(input("Enter a vulue of b: "))
#
# print("Sum is : ", a+b)
# print("Mul is : ", a*b)
# print("Div is : ", a/b)
# print("Sub is : ", a-b)
# print("integer is : ", a//b)
# print("Mod is : ", a%b)
# print("Power is : ", a**b)
# ============================================

# Program to calculate area of circle
#
# r = float(input("Enter area of Radius: "))
# pi = 3.14
# area = pi*(r**2)
# print("Area of Circle is : ", area)

#=============================================

# Enter the amount and count the note and type
#
# amt = int(input("Enter the anount you want to withdraw: "))
#
# print("2000 notes is : ", amt//2000)
# amt=amt%2000
# print("500 notes is : ", amt//500)
# amt=amt%500
# print("200 notes is : ", amt//200)
# amt=amt%200
# print("100 notes is : ", amt//100)
# amt=amt%100
# print("50 notes is : ", amt//50)
# amt=amt%50
# print("10 notes is : ", amt//10)
# amt=amt%10
# print("5 notes is : ", amt//5)
# amt=amt%5
# print("1 notes is : ", amt//1)
# amt=amt%1
# ======================================

# Create a marksheet

math = int(input("Enter the number of MATHS: "))
hindi = int(input("Enter the number of HINDI: "))
Py = int(input("Enter the number of Physics: "))
Che = int(input("Enter the number of Chemistry: "))
eng = int(input("Enter the number of Eng:"))

total = math+hindi+Py+Che+eng

pre = (total/500)*100

print("===============================")
print("Marks in Maths is :    | ", math, "|")
print("Marks in Physics is :  | ", Py, "|")
print("Marks in Chemistry is :| ", Che, "|")
print("Marks in English is :  | ", eng, "|")
print("Marks in Hindi is :    | ", hindi, "|")
print("==============================")
print("Total number is : ", total)
print("==============================")

print("% is : ", pre)