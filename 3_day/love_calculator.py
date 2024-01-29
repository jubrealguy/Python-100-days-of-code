print("This is your favourite Love Calculator")
mine = input("What is your Name: ")
yours = input("What is your spouse Name: ")
name = (mine + yours).lower()

true = ['t', 'r', 'u', 'e']
firstDigit = 0
for i in true:
    firstDigit += name.count(i)

love = ['l', 'o', 'v', 'e']
secondDigit = 0
for i in love:
    secondDigit += name.count(i)

score = int(str(firstDigit) + str(secondDigit))

if score < 10 or score > 90:
    print(f"Your score is {score}, you guys go together like coke and menthos")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you guyz go together")
else:
    print(f"Your score is {score}")
