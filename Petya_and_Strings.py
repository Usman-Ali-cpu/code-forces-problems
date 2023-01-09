def function(str1, str2):
    if len(str1) < len(str2):
        return -1
    elif len(str1) > len(str2):
        return 1
    else:
        str1 = str1.lower()
        str2 = str2.lower()
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                if str1[i] < str2[i]:
                    return -1
                else:
                    return 1
        return 0


print(function(input(), input()))