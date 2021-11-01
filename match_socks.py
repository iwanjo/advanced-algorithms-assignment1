from collections import Counter

def match_socks(n, arr):
    totalPairs = 0
    n=Counter(arr)
    for j in n:
        totalPairs += n[j] // 2
    return totalPairs

print(match_socks(10, [1, 2, 1, 3, 4, 2, 5, 4, 1, 3]))
print(match_socks(30, [1, 2, 2, 3, 4, 1, 2, 4, 6, 8, 12, 14, 11, 16, 12, 4, 1, 9, 9, 4, 1, 2, 4, 6, 8, 7, 5, 20, 12]))
print(match_socks(80, [3, 19, 19, 19, 4, 1, 2, 4, 15, 15, 11, 14, 11, 16, 12, 12, 1, 9, 9, 4, 1, 2, 4, 6, 8, 7, 5, 20, 12, 1, 2, 2, 3, 4, 1, 2, 4, 6, 8, 12, 14, 11, 16, 12, 4, 1, 9, 9, 4, 1, 2, 4, 6, 8, 7, 5, 20, 12, 1, 2, 2, 3, 4, 1, 2, 4, 6, 8, 12, 14, 11, 16, 12, 4, 1, 9, 9]))