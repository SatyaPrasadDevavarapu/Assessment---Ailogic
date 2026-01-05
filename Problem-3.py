def long_substring(string):
    start = 0
    maxLength = 0
    usedChar = {}

    for i in range(len(string)):
        if string[i] in usedChar and start <= usedChar[string[i]]:
            start = usedChar[string[i]] + 1
        else:
            maxLength = max(maxLength, i - start + 1)

        usedChar[string[i]] = i
    return maxLength

input_string = "abcabcbb"

result = long_substring(input_string)
print(result)

