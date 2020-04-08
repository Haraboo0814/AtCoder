from queue import deque

s = deque([i for i in input()])
Q = int(input())
state = 0
for _ in range(Q):
    q = input()
    if q[0] == '1':
        if state == 0:
            state = 1
        else:
            state = 0
    else:
        if int(q[2]) == 1:
            if state == 0:
                s.appendleft(q[-1])
            else:
                s.append(q[-1])
        elif int(q[2]) == 2:
            if state == 0:
                s.append(q[-1])
            else:
                s.appendleft(q[-1])

if state == 1:
    s.reverse()
print(''.join(s))
