max_v = 1000
G = [[] for i in range(max_v)]
color = [0 for i in range(max_v)]


def create_graph(n):
    E = int(input())
    for i in range(E):
        s, t = map(int, input().split())
        G[s].append(t)
        G[t].append(s)


def dfs(v, c):
    color[v] = c
    for i in range(len(G[v])):
        # 隣が同色であればFalse
        if color[G[v][i]] == c:
            return False
        # 隣が塗られてなければ-cで塗る
        if color[G[v][i]] == 0 and dfs(G[v][i], -c) == False:
            return False

    return True


def solve(n):
    create_graph(n)
    for i in range(n):
        if color[i] == 0:
            if dfs(i, 1) == False:
                print("No")
                return
    print("Yes")


solve(4)
