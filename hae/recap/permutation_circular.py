"""Permutation and circular queue

- O(8! x 15)
- Edge Case: Consider when all friends were selected
"""

from itertools import permutations
from collections import deque


def solution(n: int, weak_list: list[int], dist_list: list[int]) -> int:
    for required_friend in range(1, len(dist_list) + 1):
        dist_prmt = permutations(dist_list, required_friend)

        for dist in dist_prmt:
            for start_weak_idx in range(len(weak_list)):
                flatten_weak = deque(
                    weak_list[start_weak_idx:]
                    + [weak + n for weak in weak_list[:start_weak_idx]]
                )

                for current_dist in dist:
                    if not flatten_weak:
                        break

                    current_point = flatten_weak.popleft()
                    friend_coverage = current_point + current_dist

                    while flatten_weak and flatten_weak[0] <= friend_coverage:
                        flatten_weak.popleft()

                if not flatten_weak:
                    return required_friend

    return -1
