import math


def nb_year(p0, percent, aug, p):
    pop = p0
    years = 0

    while pop < p:
        pop = math.floor(pop + pop * (percent / 100) + aug)
        years += 1
    return years


print(nb_year(1500, 5, 100, 5000))  # 15
