#Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

#Based on a user's order, work out their final bill.

#Small Pizza: $15

#Medium Pizza: $20

#Large Pizza: $25

#Pepperoni for Small Pizza: +$2

#Pepperoni for Medium or Large Pizza: +$3

#Extra cheese for any size pizza: + $1

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
final_bill = 0
if size == "S":
    final_bill += 15
    if add_pepperoni == "Y":
        final_bill += 2
    if extra_cheese == "Y":
        final_bill += 1
elif size == "M":
    final_bill += 20
    if add_pepperoni == "Y":
        final_bill += 3
    if extra_cheese == "Y":
        final_bill += 1
elif size == "L":
    final_bill = 25
    if add_pepperoni == "Y":
        final_bill += 3
    if extra_cheese == "Y":
        final_bill += 1
else:
    print("Please use the proper input.")
print(f"Your final bill is ${final_bill}.")