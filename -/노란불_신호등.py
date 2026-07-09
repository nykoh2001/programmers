"""https://school.programmers.co.kr/learn/courses/30/lessons/468371"""

from math import gcd


def solution(signals):
    cycles = [G + Y + R for G, Y, R in cycles]
    
    lcm = 1
    for c in cycles:
        lcm = (lcm * c) // gcd(lcm, c)

    yellow_periods = [[False for _ in range(lcm + 1)] for _ in range(len(signals))]

    for idx, signal in enumerate(signals):
        G, Y, _ = signal
        current_signal_cycle = cycles[idx]
        for t in range(lcm // current_signal_cycle + 1):
            start_val = current_signal_cycle * t + G
            for i in range(Y):
                if start_val + i <= lcm:
                    yellow_periods[idx][start_val + i] = True

    for t in range(1, lcm + 1):
        current_signal = [yellow_period[t] for yellow_period in yellow_periods]
        
        if all(current_signal):
            return t + 1

    return -1


if __name__ == "__main__":
    print(solution([[1, 1, 1]])), [1, 2, 1]
