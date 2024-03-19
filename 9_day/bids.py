# from art import logo

# from os import system #for windows
# clear = lambda: system('cls')

# print(logo)
# another_bidder = True

# bid_list = []
# while another_bidder:
#     name = input("What is your name? ")
#     price = int(input("How much are you bidding? $"))
#     bid_dict = {}
#     bid_dict["name"] = name
#     bid_dict["bid"] = price
#     bid_list.append(bid_dict)
#     ans = input("Is there another bidder? Type 'yes' or 'no' ").lower()

#     if ans == 'no':
#         another_bidder = False
#     elif ans == 'yes':
#         clear()

# maxim = 0
# if another_bidder == False:
#     for i in range(len(bid_list)):
#         if bid_list[i]["bid"] > maxim:
#             maxim = bid_list[i]["bid"]

#     for j in range(len(bid_list)):
#         if bid_list[j]["bid"] == maxim:
#             print(f"The winner is {bid_list[j]['name']} with a bid of ${bid_list[i]['bid']}")


from art import logo

from os import system #for windows
clear = lambda: system('cls')

print(logo)
another_bidder = True

while another_bidder:
    name = input("What is your name? ")
    price = int(input("How much are you bidding? $"))
    bid_dict = {}
    bid_dict[name] = price
    ans = input("Is there another bidder? Type 'yes' or 'no' ").lower()

    if ans == 'no':
        another_bidder = False
    elif ans == 'yes':
        clear()

maxim = 0
if another_bidder == False:
    for item in bid_dict:
        if bid_dict[name] > maxim:
            maxim = bid_dict[name]

    if bid_dict[name] == maxim:
        print(f"The winner is {name} with a bid of ${bid_dict[name]}")