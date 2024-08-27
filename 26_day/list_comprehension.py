import random as rd

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num ** 2 for num in numbers]
even_numbers = [num for num in numbers if num % 2 == 0]
print(squared_numbers)
print(even_numbers)
