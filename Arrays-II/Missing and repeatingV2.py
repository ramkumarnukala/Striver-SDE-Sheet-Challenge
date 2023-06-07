def missingAndRepeating(arr, n):
    xr = 0
    for i in range(n):
        xr = xr ^ arr[i]
        xr = xr ^ (i + 1)
    
    pos = (xr & ~(xr - 1))
    
    one, zero = 0, 0
    for i in range(n):
        if((arr[i] & pos) == 0):
            zero = zero ^ arr[i]
        else:
            one = one ^ arr[i]
        if(((i + 1) & pos) == 0):
            zero = zero ^ (i + 1)
        else:
            one = one ^ (i + 1)
    
    counter = 0
    for i in arr:
        if(i == zero):
            counter += 1
    
    if(counter == 2):
        return [one, zero]
    return [zero, one]