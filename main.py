#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to Tip Calculator")
bill=float(input("What was your bill?"))
tip=int(input("How much percent do you want to tip:10, 12, 15?"))
tip_percent=tip/100
total_tip=bill*tip_percent
people=int(input("Among how many people do you want to split?"))

total_amount=bill+total_tip
to_pay=round(total_amount/people,2) 
to_pay="{:.2f}".format(to_pay)
print(f"Each of you has to pay {to_pay} dollars")