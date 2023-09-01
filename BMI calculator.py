height = float(input("Enter Your Height in metres: "))
weight = float(input("Enter Your Weight in kilograms: "))

BMI= weight / (height * height)

print("Your BMI is: ", round(BMI, 2))

if BMI <= 18.5:
    print("Underweight.")
elif 18.5 < BMI <= 24.9:
    print("Normal.")
elif 25 < BMI <= 29.29:
    print("Overweight.")
else:
    print("Obese.")
