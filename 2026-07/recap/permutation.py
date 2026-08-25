"""https://school.programmers.co.kr/learn/courses/30/lessons/64064

- Permutation (Brute-force)
"""

from itertools import permutations


def _is_banned(user_id: str, banned_id: str) -> bool:
    if len(user_id) != len(banned_id):
        return False

    for u, b in zip(user_id, banned_id):
        if b != "*" and b != u:
            return False

    return True


def solution(user_ids: list[str], banned_ids: list[str]) -> int:
    user_id_comb_set = set()
    num_banned_ids = len(banned_ids)

    for user_prmt in permutations(user_ids, num_banned_ids):
        is_valid_prmt = True
        for user_id, banned_id in zip(user_prmt, banned_ids):
            if not _is_banned(user_id, banned_id):
                is_valid_prmt = False
                break

        if is_valid_prmt:
            user_id_comb_set.add(tuple(sorted(user_prmt)))

    return len(user_id_comb_set)
