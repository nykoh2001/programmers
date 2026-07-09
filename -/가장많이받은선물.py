"""https://school.programmers.co.kr/learn/courses/30/lessons/258712

선물을 받는 조건:
1. 준 선물 > 받은 선물
2. 준 선물 == 받은 선물 and 총 준 선물 > 총 받은 선물

개인과 개인 사이에 주고 받은 선물을 나타내야 함
친구들의 수가 50 이하로 제한 -> 이차원 배열을 만들어도 2.5천 칸

"""

from collections import Counter


def solution(friends, gifts):

    gift_counter = Counter()

    len_friends = len(friends)
    friend_to_idx = {friend: idx for idx, friend in enumerate(friends)}
    gift_trades = [[0 for _ in range(len_friends)] for _ in range(len_friends)]
    gift_scores = [0 for _ in range(len_friends)]

    # 주고 받은 선물들을 기록
    for gift in gifts:
        giver, receiver = gift.split()
        giver_idx = friend_to_idx[giver]
        receiver_idx = friend_to_idx[receiver]

        gift_trades[giver_idx][receiver_idx] += 1

        # 선물지수 계산
        gift_scores[giver_idx] += 1
        gift_scores[receiver_idx] -= 1

    # 각 친구들 조합에 대해 주고 받은 선물 개수 비교 + 선물 지수 비교
    for i in range(len_friends):
        for j in range(i + 1, len_friends):

            str_i = str(i)
            str_j = str(j)

            i_to_j = gift_trades[i][j]
            j_to_i = gift_trades[j][i]

            # 주고 받은 선물 개수에서 차이가 난다면 다음 달에 선물을 받을 친구 즉시 결정
            if i_to_j > j_to_i:
                gift_counter.update([str_i])

            elif i_to_j < j_to_i:
                gift_counter.update([str_j])

            # 주고 받은 선물의 개수 동일
            else:
                # 선물 지수 비교
                i_gift_score = gift_scores[i]
                j_gift_score = gift_scores[j]

                # 선물 지수에서 차이가 난다면 다음 달에 선물 받을 친구 결정
                if i_gift_score > j_gift_score:
                    # gift_counter.update(str_i)
                    gift_counter.update([str_i])

                elif i_gift_score < j_gift_score:
                    # gift_counter.update(str_j)
                    gift_counter.update([str_j])

    most_common = gift_counter.most_common(1)

    # 선물 받을 친구가 결정되지 않았아면 0 반환
    if not most_common:
        return 0

    max_gift = most_common[0][1]
    return max_gift


if __name__ == "__main__":
    print(
        solution(
            ["muzi", "ryan", "frodo", "neo"],
            [
                "muzi frodo",
                "muzi frodo",
                "ryan muzi",
                "ryan muzi",
                "ryan muzi",
                "frodo muzi",
                "frodo ryan",
                "neo muzi",
            ],
        )
    )
