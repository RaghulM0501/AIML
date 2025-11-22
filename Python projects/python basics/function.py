def age_verification(age):
    return age >=18
    

age = int(input("Enter your age: "))
Veri_status = age_verification(age)
if Veri_status == True:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")