# 3:19 ~ 3:35 (8/13)
# 3: 50 - stop

from collections import defaultdict
from sys import maxsize


def solution(n: int, wires: list[list[int]]) -> int:
    min_group_size_diff = maxsize
    for removed_wire in wires:
        parents = [node for node in range(n + 1)]

        def _find(node: int) -> int:
            if node == parents[node]:
                return node
            return _find(parents[node])

        def _union(node1: int, node2: int) -> bool:
            root1, root2 = _find(node1), _find(node2)
            if root1 == root2:
                return False
            parents[root2] = root1
            return True

        for wire in wires:
            if removed_wire == wire:
                continue
            is_unioned = _union(wire[0], wire[1])
            if not is_unioned:
                break

        if not is_unioned:
            continue
        pivot_root = _find(1)

        group_size = len(
            [node for node in parents if _find(node) == pivot_root])
        min_group_size_diff = min(min_group_size_diff, abs(n - 2 * group_size))

    return min_group_size_diff
