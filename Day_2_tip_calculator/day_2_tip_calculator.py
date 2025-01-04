# Here we put in practice type casting and math operators. As well of the round function and F-strings
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip_amount = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people are splitting the bill? "))

total_bill_with_tip = ((total_bill * tip_amount) / 100) + total_bill
pay_per_person = round(total_bill_with_tip / people, 2)

print(f"Each person should pay: ${pay_per_person}")

