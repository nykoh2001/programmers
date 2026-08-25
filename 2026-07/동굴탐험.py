"""Edge case - 0에서 시작할 수 없을 때"""

from collections import defaultdict, deque


def solution(caves: int, path: list[list[int]], order: list[list[int]]) -> bool:
    graph = defaultdict(list)
    for cave1, cave2 in path:
        graph[cave1].append(cave2)
        graph[cave2].append(cave1)

    sub_pre_order = defaultdict(int)
    pre_sub_order = defaultdict(int)
    for pre, sub in order:
        if sub == 0:
            return False
        sub_pre_order[sub] = pre
        pre_sub_order[pre] = sub

    visited = [False] * caves
    visited[0] = True

    cave_to_visit = deque([0])
    cave_to_visit_later = defaultdict(int)

    while cave_to_visit:
        current_cave = cave_to_visit.popleft()

        for next_cave in graph[current_cave]:
            if visited[next_cave]:
                continue

            if sub_pre_order[next_cave] > 0:
                cave_to_visit_later[sub_pre_order[next_cave]] = next_cave
                continue

            cave_to_visit.append(next_cave)
            visited[next_cave] = True

            if pre_sub_order[next_cave]:
                sub_pre_order.pop(pre_sub_order[next_cave])

            if cave_to_visit_later.get(next_cave):
                blocked_cave = cave_to_visit_later[next_cave]
                if not visited[blocked_cave]:
                    cave_to_visit.append(blocked_cave)
                    visited[blocked_cave] = True
                cave_to_visit_later.pop(next_cave)

    for v in visited:
        if not v:
            return False

    return True
