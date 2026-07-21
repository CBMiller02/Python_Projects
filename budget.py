# This is the personal budgeting application.

income = int(input("Enter your monthly income (before tax): $"))

# Federal tax income brackets are 10, 12, 22, 24, 32, 35, and 37 percent.

pa_tax = 0.0307

state_income = income - (income * pa_tax)

if state_income <= 12400:
    post_federal_income = state_income - (state_income * 0.10)
    print("$", post_federal_income, "is what you have after Pennsylvania state income tax and Federal income tax.")

elif state_income <= 50400:
    post_federal_income = state_income - (state_income * 0.12)
    print("$", post_federal_income , "is what you have after Pennsylvania state income tax and Federal income tax.")

elif state_income <= 105700:
    post_federal_income = state_income - (state_income * 0.22)
    print("$", post_federal_income, "is what you have after Pennsylvania state income tax and Federal income tax.")

elif state_income <= 201775:
    post_federal_income = state_income - (state_income *0.24)
    print("$", post_federal_income, "is what you have after Pennsylvania state income tax and Federal income tax.")

elif state_income <= 256225:
    post_federal_income = state_income - (state_income * 0.32)
    print("$", post_federal_income, "is what you have after Pennsylvania state income tax and Federal income tax.")

elif state_income <= 640600:
    post_federal_income = state_income - (state_income * 0.35)
    print("$", post_federal_income, "is what you have after Pennsylvania state income tax and Federal income tax.")

elif state_income > 640600:
    post_federal_income = state_income - (state_income * 0.37)
    print("$", post_federal_income, "is what you have after Pennsylvania state income tax and Federal income tax.")

else:
    print("That is not a valid income.")

# Now we will move on to the budget.

print("This is your personal budget calculator.")

house = int(input("Enter your monthly rent or mortgage: $"))
groceries = int(input("Enter your monthly grocery spending: $"))
phone = int(input("Enter your monthly phone bill: $"))
internet = int(input("Enter your monthly internet bill: $"))
car_payment = int(input("Enter your monthly car payment: $"))
car_insurance = int(input("Enter your monthly car insurance: $"))
car_maint = int(input("Enter your monthly car maintenance: $"))
health = int(input("Enter your monthly health insurance: $"))
prop = int(input("Enter your monthly renters OR property insurance: $"))

total_expenses = (house + groceries + phone + internet + car_payment + car_insurance + car_maint + health + prop)
print("$", total_expenses, "is the sum of your monthly expenses.")

# Moving on to combine income and taxes.

leftover = (post_federal_income - total_expenses)
print("$", leftover, "is how much you have left, after paying US + Pennsylvania taxes and paying expenses.")

# Now we know how much is left over. Let's allocate budgeting.

print("Now we will allocate the remainder savings. Combined percentage cannot exceed 100%.")
print("We will cover 4 savings sections: Retirement Savings, Family, Travel, and Miscallaneous.")
savings = int(input("What percentage of your leftover money would you like to save for retirement? %"))
family = int(input("What percentage of your leftover money would you like to save for family needs or events? %"))
travel = int(input("What percentage of your leftover money would you like to save for travel? %"))
misc = int(input("What percentage of your leftover money would you like to save for miscellaneous items? %"))

total = savings + family + travel + misc

if total > 100:
    print("The amount you entered exceeds 100%. Please adjust the amounts.")

elif total >= 0:
    print("Thank you for your input. The sum of what you will save is: $", total)

else:
    print("That is not a valid input.")



