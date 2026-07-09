"""https://school.programmers.co.kr/learn/courses/30/lessons/389479

상태:
1. 운영 중인 서버의 개수 증설 후 k 시간동안 유지
2. 현재까지 증설된 서버 개수

증설 횟수 = active_players // m + ceil((active_players % m) / m)
"""

from math import ceil


def solution(players, m, k):
    len_players = len(players)
    active_servers = [0] * len_players
    expanded_servers = 0

    for hour, player in enumerate(players):
        # print(active_servers)
        current_active_servers = active_servers[hour]

        # 서버 증설이 필요하다면
        if current_active_servers * m < player:
            extra_player_count = player - current_active_servers * m
            new_servers = extra_player_count // m
            expanded_servers += new_servers

            # print(f"extra_player_count : {extra_player_count}")
            # print(f"{hour}: {new_servers}")
            # 새로운 서버들을 k 시간동안 증설하여 운영
            for i in range(hour, hour + k):
                if i <= len_players - 1:
                    active_servers[i] += new_servers

    # print(active_servers)
    return expanded_servers


if __name__ == "__main__":
    print(
        solution(
            [0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5],
            3,
            5,
        )
    )
