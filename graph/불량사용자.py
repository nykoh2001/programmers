"""https://school.programmers.co.kr/learn/courses/30/lessons/64064

- BitMask

Approach 1:
- Iterate user_id & banned_id, compare letter by letter or use regex
: O(U x B x L)

Approach 2: 
- DFS/Backtracking + BitMask 
"""


def is_banned(user_id: str, banned_id: str) -> bool:
    if len(user_id) != len(banned_id):
        return False

    for u, b in zip(user_id, banned_id):
        if b != "*" and u != b:
            return False

    return True


def solution(user_ids: list[str], banned_ids: list[str]) -> int:
    result = set()
    len_banned_ids = len(banned_ids)

    def check_user_ids(banned_idx: int, selected_mask: int):
        if banned_idx == len_banned_ids:
            result.add(selected_mask)
            return

        for user_idx, user_id in enumerate(user_ids):
            if selected_mask & (1 << user_idx):
                continue

            if not is_banned(user_id, banned_ids[banned_idx]):
                continue

            check_user_ids(banned_idx + 1, selected_mask | (1 << user_idx))

    check_user_ids(0, 0)
    return len(result)
