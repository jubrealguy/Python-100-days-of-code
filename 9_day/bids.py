from os import system #for windows
clear = lambda: system('cls')

another_bidder = True

bid_list = []
while another_bidder:
    name = input("What is your name? ")
    bid = int(input("How much are you bidding? $"))
    bid_dict = {}
    bid_dict["name"] = name
    bid_dict["bid"] = bid
    bid_list.append(bid_dict)
    ans = input("Is there another bidder? Type 'yes' or 'no' ").lower()

    if ans == 'no':
        another_bidder = False
    elif ans == 'yes':
        clear()

maxim = 0
if another_bidder == False:
    for i in range(len(bid_list)):
        if bid_list[i]["bid"] > maxim:
            maxim = bid_list[i]["bid"]

    for j in range(len(bid_list)):
        if bid_list[j]["bid"] == maxim:
            print(bid_list[j]["name"])

