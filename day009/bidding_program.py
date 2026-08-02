from clear import clear


def logo():
    print('''    
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\
    ''')


def auction(auctions):
    offer_name = ""
    offer_bid = 0
    for i in range(len(auctions)):
        if offer_bid < auctions[i]['bid']:
            offer_name = auctions[i]['name']
            offer_bid = auctions[i]['bid']

    print(f"The biggest bid offered is ${offer_bid} by {offer_name}")


logo()
print("Welcome to the secret auction program.")
auction_list = []
bidders_left = "yes"
while bidders_left[0] == "y":
    bidder_name = input("What's your name?: ")
    bid_amount = int(input("What is your bid?: $"))
    auction_list.append({"name": bidder_name, "bid": bid_amount})
    bidders_left = input("Are there any other bidders?: Type 'yes' or 'no' ").lower()
    clear()

auction(auction_list)
