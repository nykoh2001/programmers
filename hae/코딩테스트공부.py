"""2차원 DP
- 효율성 테스트 실패
- BFS < Daijkstra
"""

import heapq as hq


def solution(alp, cop, problems):
    INF = 10**9
    min_time_spent = INF

    problems += [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]

    max_alp = max(p[0] for p in problems)
    max_cop = max(p[1] for p in problems)

    initial_alp, initial_cop = min(alp, max_alp), min(cop, max_cop)

    dp = [[INF] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[initial_alp][initial_cop] = 0

    alp_cop_to_visit = [(0, initial_alp, initial_cop)]

    while alp_cop_to_visit:
        cost, a, c = hq.heappop(alp_cop_to_visit)

        if a >= max_alp and c >= max_cop:
            return cost

        for problem in problems:
            alp_req, cop_req, alp_rwd, cop_rwd, time = problem

            if alp_req > a or cop_req > c:
                continue

            new_alp = min(a + alp_rwd, max_alp)
            new_cop = min(c + cop_rwd, max_cop)

            if dp[new_alp][new_cop] <= cost + time:
                continue

            dp[new_alp][new_cop] = dp[a][c] + time
            hq.heappush(alp_cop_to_visit, (dp[a][c] + time, new_alp, new_cop))

    return dp[max_alp][max_cop]
