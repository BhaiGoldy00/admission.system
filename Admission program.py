import time
print("Welcome to Delhi Public School Bulandshahr , PCM Entrance Examination")

print()

time.sleep(2)

print("Enter the following details :")

time.sleep(1)

name = input("Enter Your Name -")

print("Enter your marks:")

time.sleep(1)

english = int(input("Enter your marks in English - "))
maths = int(input("Enter your marks in Maths - "))
science = int(input("Enter your marks in Science -"))

print()

percentage = (english + maths + science)/3

print("Your total Percent scored is:" , percentage)

print("Wait while we check your application for final result ")
time.sleep(2)

print()

if english > 100 or maths > 100 or science > 100 or english < 0 or maths < 0 or science < 0 : 
    print("Details are wrong , try again !")

elif percentage >= 90 :
    print("Congratulations" ,name, "your application for admission in DPS for PCM stream has been accepted.")
    
else :
    print("With regret, your application for admission has been declined because you did not fulfill the required criteria.")


