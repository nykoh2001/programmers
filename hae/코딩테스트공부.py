"""2차원 DP
- 효율성 테스트 실패
"""

from collections import deque


def solution(alp, cop, problems):
    MAX_IDX = 180
    INF = 10**9

    min_time_spent = INF

    dp = [[INF] * MAX_IDX for _ in range(MAX_IDX)]
    dp[alp][cop] = 0

    alp_cop_to_visit = deque([(alp, cop)])

    while alp_cop_to_visit:
        a, c = alp_cop_to_visit.popleft()
        if a + 1 < MAX_IDX and c < MAX_IDX and dp[a+1][c] > dp[a][c] + 1:
            dp[a + 1][c] = dp[a][c] + 1
            alp_cop_to_visit.append((a+1, c))

        if a < MAX_IDX and c + 1 < MAX_IDX and dp[a][c+1] > dp[a][c] + 1:
            dp[a][c + 1] = dp[a][c] + 1
            alp_cop_to_visit.append((a, c+1))

        all_problem_solved = True
        for problem in problems:
            alp_req, cop_req, alp_rwd, cop_rwd, time = problem

            if alp_req > a or cop_req > c:
                all_problem_solved = False
                continue

            if a + alp_rwd >= MAX_IDX or c + cop_rwd >= MAX_IDX:
                continue

            if dp[a + alp_rwd][c + cop_rwd] <= dp[a][c] + time:
                continue

            dp[a + alp_rwd][c + cop_rwd] = dp[a][c] + time
            alp_cop_to_visit.append((a + alp_rwd, c + cop_rwd))

        if all_problem_solved:
            min_time_spent = min(min_time_spent, dp[a][c])

    return min_time_spent
