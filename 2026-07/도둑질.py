"""https://school.programmers.co.kr/learn/courses/30/lessons/42897

- 1st: DP, edge case
- 2nd: DP but consider whether the first house was visited or not
  - Regarding it is circular queue
"""


def solution(money: list[int]) -> int:
    len_money = len(money)
    stolen = [[0] * len_money for _ in range(2)]
    # stolen[0]: 0번째 집을 방문하지 않았을 때
    # stolen[1]: 0번째 집을 방문했을 때
    stolen[0][0], stolen[0][1] = 0, money[1]
    stolen[1][0], stolen[1][1] = money[0], money[0]

    for house_idx, house_money in enumerate(money):
        if house_idx <= 1:
            continue

        stolen[0][house_idx] = max(
            stolen[0][house_idx - 2] + money[house_idx],
            stolen[0][house_idx - 1]
        )
        stolen[1][house_idx] = max(
            stolen[1][house_idx - 2] + money[house_idx],
            stolen[1][house_idx - 1]
        )

    return max(
        stolen[0][len_money - 1],
        stolen[0][len_money - 2],
        stolen[1][len_money - 2]
    )
