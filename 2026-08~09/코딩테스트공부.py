from collections import deque

# 3:03 ~ 3:17 - Runtime error -> ~3:28


def solution(alp, cop, problems):
    max_req_alp, max_req_cop = 0, 0
    for alp_req, cop_req, _, _, _ in problems:
        max_req_alp = max(max_req_alp, alp_req)
        max_req_cop = max(max_req_cop, cop_req)

    # Edge case - 초기 alp, cop가 이미 요구되는 최대 alp, cop보다 큰 경우 고려
    alp = min(alp, max_req_alp)
    cop = min(cop, max_req_cop)

    INF = float('inf')
    cost_dp = [[INF] * (max_req_cop + 1) for _ in range(max_req_alp + 1)]
    cost_dp[alp][cop] = 0

    # d_alp, d_cop, cost
    basic_moves = [(1, 0, 1), (0, 1, 1)]
    cells_to_visit = deque([(alp, cop)])

    while cells_to_visit:
        curr_alp, curr_cop = cells_to_visit.popleft()
        moves = basic_moves + [(alp_rwd, cop_rwd, cost) for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems
                               if curr_alp >= alp_req and curr_cop >= cop_req]

        for d_alp, d_cop, cost in moves:
            next_alp = min(curr_alp + d_alp, max_req_alp)
            next_cop = min(curr_cop + d_cop, max_req_cop)
            next_cost = cost_dp[curr_alp][curr_cop] + cost

            if cost_dp[next_alp][next_cop] <= next_cost:
                continue

            cost_dp[next_alp][next_cop] = next_cost
            cells_to_visit.append((next_alp, next_cop))

    return cost_dp[max_req_alp][max_req_cop]
