def missingAndRepeating(arr, n):
    sn = (n * (n+1))//2
    sn2 = (n * (n+1) * (2*n+1))//6
    
    s, s2 = 0, 0
    for i in arr:
        s += i
        s2 += i ** 2
    
    val1 = s - sn
    val2 = s2 - sn2
    val2 = val2 // val1
    
    x = (val1 + val2)//2
    y = x - val1
    
    return [x, y]