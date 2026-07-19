"""https://school.programmers.co.kr/learn/courses/30/lessons/42897

- 1st: DP, edge case
"""

def solution(money: list[int]) -> int:
    len_money = len(money)
    stolen = [0] * len_money
    stolen[1] = money[1]

    for house_idx, house_money in enumerate(money):
        if house_idx <= 1:
            continue

        stolen[house_idx] = max(
            stolen[house_idx - 2] + money[house_idx], stolen[house_idx - 1])

    return max(stolen[len_money - 1], stolen[len_money - 2] + money[0])
