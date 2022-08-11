print("Welcome, know your BMI and the category you fall in")
weight = float(input("What is your weight in kg: "))
height = float(input("What is your height in m: "))

bmi = weight / height ** 2
bmi_round = round(bmi, 1)

if bmi_round < 18.5:
    print(f"Your BMI is {bmi_round} amd you are Underweight.")
elif bmi_round >= 18.5 and bmi_round < 25:
    print("Your BMI is {} and you have a Normal weight".format(bmi_round))
elif bmi_round >= 25 and bmi_round < 30:
    print("Your BMI is " + bmi_round + " you are Overweight")
elif bmi_round >= 30 and bmi_round < 35:
    print(f"Your BMI is {bmi_round} and you are Obese")
else:
    print(f"Your BMI is {bmi_round} and you are Clinically obese")