# 12:19 ~ 1:58
# 문제 이해 잘못함
# 4:04 ~ 4:37
# 93.1/100

# recursion limit: 최대 깊이가 10**4


from collections import defaultdict

import sys
sys.setrecursionlimit(10**4)


def solution(nodeinfo):
    node_list = [(i, x, y) for i, (x, y) in enumerate(nodeinfo)]
    node_list.sort(key=lambda x: (-x[2], x[1]))
    visited = [False] * len(node_list)

    preorder, postorder = [], []

    def traverse(node_idx: int, left: int, right: int):
        visited[node_idx] = True
        curr_i, curr_x, curr_y = node_list[node_idx]

        preorder.append(curr_i + 1)
        for new_idx in range(node_idx + 1, len(node_list)):
            _, new_x, new_y = node_list[new_idx]
            if visited[new_idx] or new_y == curr_y:
                continue

            if new_x in range(left, curr_x):
                traverse(new_idx, left, curr_x)

            if new_x in range(curr_x + 1, right):
                traverse(new_idx, curr_x + 1, right)

        postorder.append(curr_i + 1)

    traverse(0, 0, 10 ** 5 + 1)
    return [preorder, postorder]
