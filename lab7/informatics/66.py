a = [int(a) for a in input().split()]
answer = 0
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        answer += 1
print(answer)