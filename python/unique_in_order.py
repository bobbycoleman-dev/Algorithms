s1 = "AAAABBBCCDAABBB"  # ['A', 'B', 'C', 'D', 'A', 'B']
s2 = "ABBCcAD"  # ['A', 'B', 'C', 'c', 'A', 'D']
s3 = [1, 2, 2, 3, 3]  # [1, 2, 3]
s4 = (1, 2, 2, 3, 3)  # [1, 2, 3]


def unique_in_order(s):
    result = []
    for x in range(len(s)):
        if len(result) > 0 and s[x] == result[len(result) - 1]:
            continue
        result.append(s[x])

    return result


print(unique_in_order(s1))
print(unique_in_order(s2))
print(unique_in_order(s3))
print(unique_in_order(s4))
