x = "man i need a taxi up to ubud"

alph = "abcdefghijklmnopqrstuvwxyz"
nums = {}

for i in range(len(alph)):
    nums[alph[i]] = i + 1


def high(x):
    words = x.split()
    highest_count = 0
    high_word = ""

    for word in words:
        total = 0
        for letter in word:
            total += nums[letter]

        if total > highest_count:
            highest_count = total
            high_word = word

    return high_word


print(high(x))
