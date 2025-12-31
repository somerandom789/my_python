n = int(input(f" Enter number of cycles: "))
ans = ans_1 = ans_2 = 0
for x in range(n):
    a = int(input(f" Enter number: "))
    if a > 0:
        ans += 1
    elif a == 0:
        ans_1 += 1
    else:
        ans_2 += 1
print(ans, ans_1, ans_2)





