# 5:54 ~ 6:23

# 예외 검증
# - 반대(왼쪽)로 이동하는 경우
# - A가 여러 개 연속된 경우
# - 회전 방향 정하는 조건

# 59.3 / 100

# 이동하다가 방향을 바꿔서 이동하는게 제일 빠른 경우

def _calculate_diff(letter: chr) -> int:
    if 'A' == letter:
        return 0
    return min(ord(letter) - ord('A'), ord('Z') - ord(letter) + 1)


def solution(name):
    total_diff = 0
    for letter in name:
        total_diff += _calculate_diff(letter)

    min_diff = 10 ** 9
    for idx in range(len(name)):
        next_idx = idx + 1

        while next_idx < len(name) and name[next_idx] == "A":
            next_idx += 1

        right_then_left = 2 * idx + (len(name) - next_idx)
        left_then_right = 2 * (len(name) - next_idx) + idx
        min_diff = min(min_diff, right_then_left, left_then_right)

    return total_diff + min_diff
