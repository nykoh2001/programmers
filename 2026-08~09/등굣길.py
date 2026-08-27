# 최단 거리는 항상 맨해튼임
# 위나 왼쪽으로 이동하는 경우는 결국 맨해튼보다 큰 거리 값을 가지므로 해당하지 않음
# dp[x][y] = dp[x-1][y] + dp[x][y-1]

def solution(m: int, n: int, puddles: list[list[int]]) -> int:
    MOD = 1_000_000_007
    path_count = [[0] * (n + 1) for _ in range(m + 1)]

    for x in range(1, m+1):
        for y in range(1, n+1):
            if [x, y] == [1, 1]:
                path_count[1][1] = 1
                continue
            if [x, y] in puddles:
                continue
            current_path_count = 0
            if x > 1:
                current_path_count += path_count[x-1][y] % MOD
            if y > 1:
                current_path_count += path_count[x][y-1] % MOD
            path_count[x][y] = current_path_count % MOD

    return path_count[m][n]
