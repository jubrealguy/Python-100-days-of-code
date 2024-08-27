with open('file_1.txt') as file:
    file_1_list = file.readlines()

with open('file_2.txt') as file:
    file_2_list = file.readlines()

# num1_list = [int(num.strip()) for num in file_1_list]
# num2_list = [int(num.strip()) for num in file_2_list]

# common_num_list = [num for num in num1_list if num in num2_list]
# print(int(file_1_list[0]))

common_num_list = [int(num) for num in file_1_list if num in file_2_list]
print(common_num_list)