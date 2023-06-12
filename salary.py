salary = int(input("Enter your Salary: "))

# if( n <= 10000 ):
#     da = 0.105*n
#     ta = 0.105*(n-da)
#     hra = 0.115*(n - ta)
#     pf = 0.135*(n - hra)
#     lic = 0.105*(n - pf)
#     total=da+ta+hra+pf+lic
#     print(lic,"\n", da,"\n",ta,"\n")
#     print(n-total)

if( salary <= 10000 ):
    da = 0.105*salary
    ta = 0.105*salary
    hra = 0.115*salary
    pf = 0.135*salary
    lic = 0.105*salary
    total=da+ta+hra+pf+lic
    print("Daily allowance is: ", da)
    print("TA is: ", ta)
    print("House rent allowance is: ", hra)
    print("Provient Fund is: ", pf)
    print("LIC is: ", lic)
    print("Now your salary is left: ",salary-total," from ",salary)
else:
    da = 0.115*salary
    ta = 0.115*salary
    hra = 0.135*salary
    pf = 0.155*salary
    lic = 0.115*salary
    total=da+ta+hra+pf+lic
    print("Daily allowance is: ", da)
    print("TA is: ", ta)
    print("House rent allowance is: ", hra)
    print("Provient Fund is: ", pf)
    print("LIC is: ", lic)
    print("Now your salary is left: ",salary-total," from ",salary)