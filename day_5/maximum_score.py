scores_str = input("Enter the scores of the students separated by a space:\n")
scores = scores_str.split()

for n in range(0, len(scores)):
    scores[n] = int(scores[n])

max_score = 0

for each_score in scores:
    if each_score > max_score:
        max_score = each_score
print(f'The highest score in the list of scores is {max_score}')