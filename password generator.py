import random as rd
def password(a):
    l='' 
    for i in range(a-4):
        k = str(chr(rd.randint(97,122)))
        l += k
    l += str(chr((rd.randint(33,46))))
    for k in range(2):
        l += str(chr((rd.randint(47,57))))
    l=str(chr(rd.randint(65,90)))+l    
    return l        
print("---The Password must be more than 7 characters")

a = int(input("Enter the length of the password: "))
if a>=8:

    print(f"Your password is :{password(a)}")
else:
    print("Sorry!, Please enter the length of password atleast 8, try again...")
