def solution(numbers: list[int]) -> list[int]:
    results = []
    for number in numbers:
        k_idx = 0
        k = 1
        while 2 ** k - 1 < number:
            k = 2 ** k_idx - 1
            k_idx += 1

        number_string = ""
        current_number = number
        for pow_val in range(k - 1, -1, -1):
            if 2 ** pow_val <= current_number:
                number_string += "1"
                current_number -= 2 ** pow_val
                continue
            number_string += "0"

        def _is_valid(start: int, end: int) -> bool:
            root_idx = (start + end) // 2

            if root_idx % 2 == 0:
                return True

            if number_string[root_idx] == "0":
                for idx in range(start, end):
                    if number_string[idx] == "1":
                        return False

            return _is_valid(start, root_idx) and _is_valid(root_idx + 1, end)

        is_valid = _is_valid(0, k)
        results.append(1 if is_valid else 0)

    return results
