# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / height ** 2)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")

#if bmi < 18.5:
#  bmi_result = "are underweight."
#elif bmi >= 18.5 and bmi < 22:
#  bmi_result = "have a normal weight."
#elif bmi >= 22 and bmi < 28:
#  bmi_result = "are slightly overweight."
#elif bmi >= 28 and bmi < 33:
#  bmi_result = "are obese."
#else:
#  bmi_result = "are clinically obese."
#print("Your BMI is " + str(int(bmi)) + ", you " + bmi_result)
