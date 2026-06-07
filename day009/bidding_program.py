from clear import clear
def logo():
    print ('''    
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

def auction(name, bid):
    offer_name = ""
    offer_bid = 0
    auction_list.append({'Name': name, 'bid': bid})
    name_big_bid=""
    for i in range(len(auction_list)):
        if offer_bid < auction_list[i]['bid']:
            offer_name = auction_list[i]['Name']
            offer_bid = auction_list[i]['bid']
    if biders_left[0] == "n":
        clear()
        print(f"The biggest bid offered is ${offer_bid} by {offer_name}")

    else:
        clear()


logo()
print("Welcome to the secret auction program.")
auction_list = []
biders_left = "yes"
while biders_left[0]=="y":
    name = input("What's your name?: ")
    bid = int(input("What is your bid?: $"))
    biders_left = input("Are there any other biders?: Type 'yes' or 'no' ").lower()
    auction(name,bid)

