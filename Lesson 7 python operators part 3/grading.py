m1=int(input("Marks1="))
m2=int(input("Marks2="))
m3=int(input("Marks3="))
m4=int(input("Marks4="))
sum=m1+m2+m3+m4
avg=sum//4
print("your average is",avg)
if avg<=100 and avg>90:
    print("Grade A")
elif avg<=90 and avg>80:
    print("Grade B")
elif avg<=80 and avg>70:
    print("Grade C")
elif avg<=70 and avg>60:
    print("Grade D")
else:
    print("You have failed")