N = int(input())
doc = [int(x) for x in input().split() if int(x) % 2 == 0]
for i in doc:
    if i % 3 != 0 and i % 5 != 0:
        print('DENIED')
        exit()
print('APPROVED')
