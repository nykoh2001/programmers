"""https://school.programmers.co.kr/learn/courses/30/lessons/389478

가장 윗층과 꺼내려는 상자 사이에 있는 중간 택배 상자들이 쌓이는 방향은 중요하지 않다.

1. (n - 1) // w -> p1, n % w or w -> p2
2. (num - 1) // w -> q1, num % w or w -> q2
-- p1, q1: 가장 마지막 상자/꺼내려는 상자 밑에 있는 상자의 개수 (상자가 위치한 층 - 1)
-- p2, q2: 상자가 있는 층에 있는 상자의 총 개수
3. p1, q1이 홀수라면: 오른쪽부터 쌓임
   p1, q1이 짝수라면: 왼쪽부터 쌓임
"""


def solution(n, w, num):
    p1 = (n - 1) // w
    p2 = n % w or w

    q1 = (num - 1) // w
    q2 = num % w or w

    # 맨 윗층과 꺼내려는 상자 사이에 있는 층의 개수만큼은 무조건 상자를 꺼내야 함, 초기값으로 설정
    boxes = p1 - q1

    is_p1_odd = p1 % 2
    is_q1_odd = q1 % 2

    # 두 상자가 쌓이는 방향이 같고 맨 윗층에 쌓인 상자가 꺼내려는 상자까지의 개수보다 같거나 많다면
    if is_p1_odd == is_q1_odd and p2 >= q2:
        boxes += 1

    # 두 상자가 쌓이는 방향이 다르고 맨 윗층에 쌓인 상자 개수와 꺼내려는 상자까지의 개수 합이 전체 폭에 해당하는 상자 수보다 많다면
    elif is_p1_odd != is_q1_odd and w <= p2 + q2:
        boxes += 1

    return boxes


if __name__ == "__main__":
    print(solution(13, 3, 6))
