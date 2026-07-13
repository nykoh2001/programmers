"""https://school.programmers.co.kr/learn/courses/30/lessons/60062

- Dynamic Programming
- DFS + backtracking
-> While simulating all possible cases, update the min valud of friends

- 시작점이 없다
- 각 weak point마다 친구를 무조건 배정해야 함

Approach 1:
- DFS + Backtracking: Timeout for the 2nd test case
=> Condition check within the while loop
"""


def solution(n, weak, dist):
    INF = float('inf')
    required_friends = INF
    repaired_bitmask = 1
    len_weak = len(weak)
    len_dist = len(dist)

    for i in range(1, len_weak):
        repaired_bitmask |= (1 << i)

    def allocate_friends(
        weak_idx: int, weak_bitmask: int, dist_bitmask_str: str
    ):
        nonlocal required_friends
        friend_count = dist_bitmask_str.count("1")
        
        if weak_bitmask == repaired_bitmask:
            required_friends = min(required_friends, friend_count)
            return

        if friend_count >= required_friends:
            return

        for dist_idx, dist_bitmask in enumerate(dist_bitmask_str):
            if dist_bitmask == "1":
                continue

            new_dist_bitmask_str = (
                dist_bitmask_str[:dist_idx]
                + "1"
                + dist_bitmask_str[dist_idx + 1:]
            )
            dist_start = weak[weak_idx]
            dist_end = (weak[weak_idx] + dist[dist_idx]) % n

            new_weak_bitmask = weak_bitmask
            new_weak_idx = weak_idx
            while (
                (weak[new_weak_idx] >= dist_start
                 and weak[new_weak_idx] <= dist_end)
                or (dist_start > dist_end
                    and weak[new_weak_idx] >= dist_start
                    and weak[new_weak_idx] <= n)
                or (
                    dist_start > dist_end
                    and weak[new_weak_idx] >= 0
                    and weak[new_weak_idx] <= dist_end
                )
            ):
                new_weak_bitmask |= (1 << new_weak_idx)
                new_weak_idx = (new_weak_idx + 1) % len_weak
                # Condition check within the while loop
                if new_weak_bitmask == repaired_bitmask:
                    break

            allocate_friends(new_weak_idx, new_weak_bitmask,
                             new_dist_bitmask_str)

    for weak_idx in range(len_weak):
        allocate_friends(weak_idx, 0, "0" * len_dist)

    return required_friends if required_friends < INF else -1
