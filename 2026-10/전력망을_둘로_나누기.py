# 3:35 ~ 3:53

def solution(n, wires):

    def _find(node: int, parents: list[int]) -> int:
        if parents[node] == node:
            return node

        return _find(parents[node], parents)

    def _union(node1: int, node2: int, parents: list[int]) -> bool:
        root1 = _find(node1, parents)
        root2 = _find(node2, parents)

        if root1 == root2:
            return False

        parents[root2] = root1
        return True

    min_diff = 10 ** 9
    for remove_idx, remove_wire in enumerate(wires):
        parents = [i for i in range(n + 1)]
        for wire_idx, wire in enumerate(wires):
            if wire_idx == remove_idx:
                continue

            node1, node2 = wire
            _union(node1, node2, parents)

        group_size = 0
        pivot = _find(parents[1], parents)
        for node in parents[1:]:
            if pivot == _find(node, parents):
                group_size += 1

        min_diff = min(min_diff, abs(n - 2 * group_size))

    return min_diff
