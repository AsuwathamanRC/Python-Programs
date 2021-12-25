logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
dict = {}

def auction(dict):
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    
    nextBidder = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    dict[name] = bid
    if nextBidder == "yes":
        auction(dict)
    else:
        max = 0
        winner = ""
        for bidder in dict:
            if dict[bidder] > max:
                max = dict[bidder]
                winner = bidder
        
        print(f"The winner is {winner} with a bid of ${max}")

auction(dict)