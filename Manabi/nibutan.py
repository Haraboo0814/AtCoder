l = [0, 0, 0, 0, 0, 0, 1, 2, 2, 2]


def binarySearch():
    left = 0
    right = len(l)
    while left < right:
        mid = (left + right) // 2
        if l[mid] == 2:
            right = mid
        elif l[mid] == 0:
            left = mid + 1
        else:
            print(mid)
            break


binarySearch()
