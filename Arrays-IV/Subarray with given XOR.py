from collections import defaultdict

def subarraysWithSumK(a: [int], b: int) -> int:
    map = defaultdict(int)
    n = len(a)
    cnt = 0
    xor = 0
    map[xor] = 1
    for i in a:
        xor ^= i
        x = xor ^ b
        cnt += map[x]
        map[xor] += 1
    return cnt