def longeststring(data):
    left = 0
    max_length = 0
    char_data = set()
    longstring = ""


    for right in range(len(data)):
        while data[right] in char_data:
            char_data.remove(data[left])
            left += 1
        char_data.add(data[right])

        if right - left + 1 > max_length:
            max_length= right -left + 1
            longstring = data[left:right+1]

    return longstring

















print(longeststring("abcabcbb"))
