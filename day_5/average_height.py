heights_str = input("Enter heights of every boy in the hall separated by a space:\n")
heights = heights_str.split()

sum_heights = 0
num_heights = 0

for person_height in heights:
    sum_heights += float(person_height)

#for num in range(0, len(height)):

for person in heights:
    num_heights += 1
    
mean = sum_heights/num_heights
print(round(mean))