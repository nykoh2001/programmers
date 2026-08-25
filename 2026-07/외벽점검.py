"""https://school.programmers.co.kr/learn/courses/30/lessons/60062

- Dynamic Programming
- DFS + backtracking
-> While simulating all possible cases, update the min valud of friends

- 시작점이 없다
- 각 weak point마다 친구를 무조건 배정해야 함

Approach 1:
- DFS + Backtracking: Timeout for the 2nd test case
=> Condition check within the while loop

Approach 2:
- Permutations of distances, iterating start point
"""

from itertools import permutations


def _check_availability(len_weak: int, weak: list[int], dist: list[int]) -> bool:
    weak_idx = 0
    for d in dist:
        end_point = weak[weak_idx] + d

        while weak[weak_idx] <= end_point:
            weak_idx += 1
            if weak_idx == len_weak:
                return True

    return False


def solution(n, weak, dist):
    len_weak = len(weak)
    for friend_count in range(1, len(dist) + 1):
        for friend_prmt in permutations(dist, friend_count):
            current_weak = weak
            for idx in range(len_weak):
                availble = _check_availability(
                    len_weak, current_weak, friend_prmt)
                if availble:
                    return friend_count

                current_weak = weak[idx:] + [w + n for w in weak[:idx]]

    return -1
