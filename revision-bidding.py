#initialization
Reserve_price = 0
name = str
age = int
won = False
bid = float
highest_bid = float
names = []
bids = []
highest_bid = 0
name = ""
while type(Reserve_price) != float:
	try:
		Reserve_price = float(raw_input("what is your the reserve price?"))
	except:
		print("please enter as a number. no letters or symbols")
#the auction
print("Auction has started")
while name.upper() !="F":
    bid = 0
    name = raw_input("what is your name?")
    if name.upper() != "F":
	    while type(bid) != float:
		try:
		    bid = float(raw_input("how much would you like to bid? please enter in numbers"))
		except:
		    print("Sorry but you need to enter a number.")
	    if bid > highest_bid:
		highest_bid = bid
		print("highest bid is $"+ str("{:.2f}".format(bid)))
		names.append(name)
		bids.append(bid)
	    else:
		print("Sorry you need to bid higher.")
#the end
if len(names) > 0:
	if bids[-1] >= Reserve_price:
		print("Auction won by " + str(names[-1]) + " with a bid of $" + str(highest_bid))
	else:
		print("Auction did not meet the reserve price")

	for i in range (0,len(names)):
		print(str(names[i]) + " bid $" + ("{:.2f}".format(bids[i])))
