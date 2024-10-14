
# try:
#     file = open('file.txt')
# except:
#     file = open('file.txt', "w")
#     file.write('something')
# else:
#     file.read()
# finally:
#     file.close()

# height = float(input("Height: "))
# weight = float(input("Weight: "))

# if height > 3:
#     raise ValueError("Height should be less than 3m")

# bmi = weight / height ** 2

# print(bmi)

# ********************   INDEX ERROR   ************************
fruits = ["Apple", "Pear", "Orange"]

def make(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("fruit pie")
    else:
        print(f"{fruit} pie")

make(3)

# ******************** KEY ERRPR *********************************
facebook_posts = [
    {"likes" : 21, "comments": 2},
    {"likes" : 13, "comments": 2, "shares" : 1},
    {"likes" : 33, "comments": 8, "shares" : 3},
    {"comments" : 4, "shares": 2},
    {"comments" : 1, "shares": 1},
    {"likes" : 19, "comments": 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes += post['likes']
    except KeyError:
        post["likes"] = 0
        # Pass too works or total_likes += 0

print(total_likes)