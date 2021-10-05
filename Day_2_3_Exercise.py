# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
max_age = 90

age_left = max_age - int(age)

total_days_left = age_left * 365
total_weeks_left = age_left * 52
total_months_left = age_left * 12

print("You have " + str(total_days_left) + " days, " + str(total_weeks_left) + " weeks, and " + str(total_months_left) + " months left.")

#years = 90 - int(age)
#months = round(years * 12)
#weeks = round(years * 52)
#days = round(years * 365)

#print(f"You have {days} days, {weeks} weeks, and {months} months left.")