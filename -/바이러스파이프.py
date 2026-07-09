"""https://school.programmers.co.kr/learn/courses/30/lessons/468373

매 순간마다 감염체와 비감염체를 연결하는 빈도가 가장 높은 파이프를 열어야 한다.
1. 감염체를 관리하는 집합 S 선언
2. 각 edge들에 대해 한 쪽 끝의 노드가 감염체이고 다른 한 쪽의 노드가 비감염체인 경우 count
3. 파이프 종류 별로 가장 많이 감염시킬 수 있는 파이프 개방
4. S 업데이트
5. 2~4를 k번 반복
6. S의 크기 반환

-- Greedy: 오답
"""


def solution(n, infection, edges, k):
    infected = set([infection])
    for iter in range(k):
        pipes = [0] * 4
        affected_nodes = [[] for _ in range(4)]
        for edge in edges:
            x, y, type = edge
            is_x_infected = int(x in infected)
            is_y_infected = int(y in infected)

            # 엣지의 양 끝 노드 중 하나만 감염체일 때, 새로운 개체를 감염시킬 수 있는 경우
            if is_x_infected + is_y_infected == 1:
                pipes[type] += 1
                if is_x_infected:
                    affected_nodes[type].append(x)
                elif is_y_infected:
                    affected_nodes[type].append(y)

        # 가장 많은 영향을 주는 파이프 선택
        pipe_to_open = [0, 0]
        for idx, pipe in enumerate(pipes):
            if pipe > pipe_to_open[1]:
                pipe_to_open[0] = idx
                pipe_to_open[1] = pipe

        # 해당 파이프를 열고 인접한 비감염체들을 감염시킴
        print(f"Open pipe: {pipe_to_open[0]}")
        infected.update(affected_nodes[pipe_to_open[0]])

    return len(infected)


if __name__ == "__main__":
    print(
        solution(
            10,
            1,
            [
                [1, 2, 1],
                [1, 3, 1],
                [1, 4, 3],
                [1, 5, 2],
                [5, 6, 1],
                [5, 7, 1],
                [2, 8, 3],
                [2, 9, 2],
                [9, 10, 1],
            ],
            2,
        )
    )
