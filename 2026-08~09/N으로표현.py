# 3:39 ~ 4:02

def solution(N: int, number: int) -> int:
    number_variations = [None]
    number_variations.append(set([N]))
    if N == number:
        return 1

    for number_freq in range(2, 9):
        num_str = f"{N}" * number_freq
        number_variations.append(set())
        number_variations[number_freq].add(int(num_str))

        for num1_idx in range(1, number_freq // 2 + 1):
            num1_set = number_variations[num1_idx]
            num2_set = number_variations[number_freq - num1_idx]

            curr_variations = []
            for num1 in num1_set:
                for num2 in num2_set:
                    curr_variations.append(num1 + num2)
                    curr_variations.append(num1 * num2)
                    if abs(num1 - num2) > 0:
                        curr_variations.append(abs(num1 - num2))
                    if (min(num1, num2) > 0):
                        curr_variations.append(
                            max(num1, num2) // min(num1, num2))

            number_variations[number_freq].update(curr_variations)
            if number in number_variations[number_freq]:
                return number_freq

    return -1
