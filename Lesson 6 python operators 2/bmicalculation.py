weight=float(input("enter ur weight in kg:"))
height=float(input("enter ur height in m:"))
bmi=weight/(height**2)
print("your BMI is",bmi)

if bmi<=18.5:
    print("you are underweight")
elif bmi<=24.9:
    print("you are healthy")
elif bmi<=29.9:
    print("you are overweight")
elif bmi<=34.9:
    print("you are obese")
else:
    print("you are extremly obese")