participants = int(input(f"Enter number of participants: "))
best_score = 0
zero_score = 0
if 1 <= participants <= 50:
    for a in range(participants):
        score = int(input(f"Enter the number of correct answers: "))
        if score == 0:
            zero_score = True
        elif score > best_score:
            best_score = score
    print(f"the best score is:{best_score}.")
    if zero_score:
        print(f"Yes")
    else:
        print(f"No")
else:
    print(f"Wrong number of participants.")



