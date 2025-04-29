print("\nBMI CALCULATOR\n")


def Bmi_calc(weight, height):
    bmi = weight / (height ** 2)
    return bmi 


def check_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))


bmi = Bmi_calc(weight, height)

category = check_bmi(bmi)


print(f"\nYour BMI is: {bmi:.2f}")
print(f"You are: {check_bmi(bmi)}")
