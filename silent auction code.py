from replit import clear
from art import logo
print(logo)
count = True
dict = {}
def findlargest(record):
    higgest_bid = 0
    for bidder in record:
        bid_amount = record[bidder]
        if bid_amount> higgest_bid:
            higgest_bid = bid_amount
            winner = bidder
    print("the highest bidder is ",winner)
    print("his bidding was :", higgest_bid)

while count == True:
    name = input("Enter Bidder's name = ")
    bid = int(input("Enter Your Bid = "))
    dict[name] = bid
    c = input("is there any more bidders left \n if yes write \'Y\' if no then write 'n' ")
    answer = c.lower()
    if answer == "y":
        clear()
    if answer =="n":
        count= False
        findlargest(dict)




