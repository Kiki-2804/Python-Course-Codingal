Amount=int(input("Enter the amount you want to withdraw:"))
Note500=Amount//500
Note100=(Amount%500)//100
Note50=((Amount%500)%100)//50
Note10=(((Amount%500)%100)%50)//10
print("Number of notes of 500 will be:", Note500)
print("Number of notes of 100 will be:", Note100)
print("Number of notes of 50 will be:", Note50)
print("Number of notes of 10 will be:", Note10)