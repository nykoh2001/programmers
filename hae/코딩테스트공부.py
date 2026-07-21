"""2차원 DP
- 효율성 테스트 실패
"""

from collections import deque


def solution(alp, cop, problems):
    INF = 10**9

    max_alp = max(p[0] for p in problems)
    max_cop = max(p[1] for p in problems)

    initial_alp, initial_cop = min(alp, max_alp), min(cop, max_cop)

    dp = [[INF] * (max_cop + 1) for _ in range(max_alp + 1)]
    dp[initial_alp][initial_cop] = 0

    alp_cop_to_visit = deque([(initial_alp, initial_cop)])

    while alp_cop_to_visit:
        a, c = alp_cop_to_visit.popleft()
        if a < max_alp and dp[a+1][c] > dp[a][c] + 1:
            dp[a + 1][c] = dp[a][c] + 1
            alp_cop_to_visit.append((a+1, c))

        if c < max_cop and dp[a][c+1] > dp[a][c] + 1:
            dp[a][c + 1] = dp[a][c] + 1
            alp_cop_to_visit.append((a, c+1))

        for problem in problems:
            alp_req, cop_req, alp_rwd, cop_rwd, time = problem

            if alp_req > a or cop_req > c:
                continue

            new_alp = min(a + alp_rwd, max_alp)
            new_cop = min(c + cop_rwd, max_cop)

            if dp[new_alp][new_cop] <= dp[a][c] + time:
                continue

            dp[new_alp][new_cop] = dp[a][c] + time
            alp_cop_to_visit.append((new_alp, new_cop))

    return dp[max_alp][max_cop]
