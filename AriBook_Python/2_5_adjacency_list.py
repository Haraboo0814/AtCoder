MAX_V = 10000000
G = [[] for i in range(MAX_V)]


def main():
    V, E = map(int, input())
    for i in range(E):
        s, t = map(int, input())
        G[s].append(t)
        # G[t].append(s)
