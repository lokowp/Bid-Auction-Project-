from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)

def add_new_bidders(new_name, new_bid):
  new_bidders_log = {}
  new_bidders_log["name"] = new_name
  new_bidders_log["bid"] = new_bid
  bidders_log.append(new_bidders_log)

def find_highest_bidder(bidders_log):
  highest_bid = 0
  winner = ""
  for bidder in bidders_log:
    name = bidder["name"]
    bid_amount = bidder["bid"]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = name
  print(f"The winner is {winner} with a bid of ${highest_bid}")
  
name = input("What is your name? ")
bid = int(input("What is your Bid price? $"))
more_bidders = input("Are there any other bidders? Yes or no? ").lower()

bidders_log = [
{
  "name": name,
  "bid": bid,
}
]


while more_bidders == "yes":
  clear()
  new_name = input("What is your name? ")
  new_bid = int(input("What is your Bid price? $"))
  more_bidders = input("Are there any other bidders? Yes or no? ").lower()
  add_new_bidders(new_name, new_bid)
clear()

find_highest_bidder(bidders_log)

