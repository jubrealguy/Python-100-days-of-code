total_number = 0

# for number in range(2, 100, 2):
#     total_number += number
# print(total_number)

for number in range(2, 100):
    if number % 2 == 0:
        total_number += number
print(total_number)