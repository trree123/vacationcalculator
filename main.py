import math
from math import sqrt
import sys
import time



# Simple Code For the Beggining
print("Welcome to the Travel Calculator")
name = input("Please Enter Your Name To Proceed: ")
if name.isalpha():
    print("Great", name , "Let's Start!")
    time.sleep(1)
else:
    print("I did not understand that, Please restart")




# We calculate the Price of The Hotel

print("Please Enter The Daily Price For Your Hotel: ")
hotel_cost_per_day = int(input())

print("Please Enter The Amount of Days You are Going to stay: ")
hotel_length = int(input())

time.sleep(1)

def hotel_cost():
  return hotel_cost_per_day * hotel_length

# We Calculate The Price Of The Airplane Ticket

print("Please Enter The Price Of The Plane Ticket: ")
airplane_ticket = int(input())

time.sleep(1)

def airplane_cost():
    return airplane_ticket

#We Calculate Additional Costs

print("Please Enter Additional Costs:")
additional_costs = int(input())

time.sleep(1)
print("Thank You For Using Travel Calculator!")
time.sleep(1)

print("Calculating your costs")
time.sleep(2)
def additional_money_spent():
    return additional_costs

print(additional_money_spent() + airplane_cost() + hotel_cost(),"$ !")

