kg = float(0)
pound = float(0)
def lbkg():
    kg = float(input("Number of Pounds: "))
    x = kg * 2.20462
    x = round(x, 3)
    print(x,"Kg")
    
def kglb():
    pound = float(input("Number of Kilograms: "))
    x = pound/2.20462
    x = round(x, 3)
    print(x,"lbs")
    

answer = input("What do you want to convert:\nKg to lbs: 1\nlbs to Kg: 2\n")
if answer == str(2):
    lbkg()
elif answer == str(1):
    kglb()
else:
    print("Not recognised")