"""Graph, Brute-force"""

def solution(key: list[list[int]], lock: list[list[int]]) -> bool:
    len_key, len_lock = len(key), len(lock)
    lock_position, key_position = [], []
    for lock_row in range(len_lock):
        for lock_col in range(len_lock):
            if not lock[lock_row][lock_col]:
                lock_position.append((len_key-1+lock_row, len_key-1+lock_col))
    lock_position.sort()

    for key_row in range(len_key):
        for key_col in range(len_key):
            if key[key_row][key_col]:
                key_position.append((key_row, key_col))
    key_position.sort()

    def _rotate(key: tuple) -> tuple:
        return (key[1], len_key - key[0])

    rotated_key = [key_position]
    current_key = key_position
    for _ in range(3):
        rotated = list(map(_rotate, current_key))
        current_key = rotated
        rotated.sort()
        rotated_key.append(rotated)

    def _is_in_valid_range(value: int) -> bool:
        return value in range(len_key - 1, len_key + len_lock - 1)

    def _is_compatible(
        key_list: list[list[int]], base_row: int, base_col: int
    ) -> bool:
        k_idx, l_idx = 0, 0
        while k_idx < len(key) and l_idx < len(lock_position):
            k = key[k_idx]
            k_r, k_c = k[0] + base_row, k[1] + base_col
            if (
                not _is_in_valid_range(k_r)
                or not _is_in_valid_range(k_c)
            ):
                k_idx += 1
                continue

            l = lock_position[l_idx]
            if k_r > l[0] or k_r < l[0] or k_r != l[0] or k_c != l[1]:
                return False

            k_idx += 1
            l_idx += 1

        if l_idx >= len(lock_position):
            return True

        return False

    # rotated_key: 4개의 회전된 키 위치 값들
    # Lock 위치: (M-1+x, M-1+y)
    # valid_range: M-1 ~ M+N-2
    for key_upper_bound in range(len_key + len_lock):
        for key_left_bound in range(len_key + len_lock):
            for key in rotated_key:
                if _is_compatible(key, key_upper_bound, key_left_bound):
                    return True
    return False
