subject1 = float(input("Enter marks obtained in subject 1: "))
subject2 = float(input("Enter marks obtained in subject 2: "))
subject3 = float(input("Enter marks obtained in subject 3: "))
totalmarks = subject1 + subject2 + subject3
percentage = (totalmarks / 300) * 100
if (percentage >= 80):
    print("Grade A")
elif(percentage>=20):
    print("Grade is B")
elif(percentage>=70):
    print("grade C")
else:
    print("fail")
    

