import heapq as hq


def solution(A: list[int], B: list[int]) -> int:
    hq.heapify(A), hq.heapify(B)
    score = 0

    while A and B:
        while A and B and A[0] >= B[0]:
            hq.heappop(B)

        while A and B and A[0] < B[0]:
            hq.heappop(A)
            hq.heappop(B)
            score += 1

    return score
