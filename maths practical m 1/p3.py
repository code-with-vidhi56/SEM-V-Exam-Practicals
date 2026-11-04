#17,5,29,12,2
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
m = int(input("Enter modulus: "))
print("\n---Propertise of congruence")
if(a-a)%m==0:
    print("1.Reflexive Property: True")
if(a-b)%m==0:
    print("2.Symmetric Property: True")
if(a-b)%m==0 and (b-c)%m==0:
    if (a-c)%m==0:
        print("3.Transitive Property: True")
if(a-b)%m==0:
    if(a+c-(b+c))%m==0:
         print("4.Addition Property: True")
if(a-b)%m==0:
    if(a-c-(b-c))%m==0:
         print("5.Subtraction Property: True")
if(a-b)%m==0:
    if(a*c-b*c)%m==0:
         print("6.Multiplication Property: True")
n = int(input("enter power n:"))
if(a-b)%m==0:
    if(a**n-b**n)%m==0:
        print("7.Power Property:True")










        
