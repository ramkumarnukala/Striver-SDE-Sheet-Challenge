def uniqueSubstrings(input_string):
    max_length = 0
    left = 0
    right = 0
    hashmap = [-1] * 256

    while right < len(input_string):
        if hashmap[ord(input_string[right])] != -1:
            left = max(hashmap[ord(input_string[right])] + 1, left)
        hashmap[ord(input_string[right])] = right
        max_length = max(max_length, right - left + 1)
        right += 1

    return max_length