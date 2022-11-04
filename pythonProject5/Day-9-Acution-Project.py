import os
from hammer_logo import logo
from time import sleep

#HINT: You can call clear() to clear the output in the console.
print(logo)
print('Welcome to the secret auction program.')
sleep(3)

end_of_auction = False
bid_dictionary = {}

while not end_of_auction:
    name = input("What is your name?\n")
    bid = input("What is your bid?\n $")
    bid_dictionary [name] = bid
    # def add_new_bid (name, bid):
    #
    #     bid_dictionary [name] = bid
    #     #print(bid_dictionary)
    #
    # add_new_bid(name, bid)
    other_bidders = input("Are there other bidders? Type [Y] or [N]\n")

    if other_bidders == "n":
        end_of_auction = True
    elif other_bidders == "y":
        os.system('cls')



max_value = max(bid_dictionary.values())
max_key = max(bid_dictionary, key=bid_dictionary.get)

print(f'The highest bidder is {max_key} with a bid of ${max_value}!')
