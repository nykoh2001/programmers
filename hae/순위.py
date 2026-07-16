"""https://school.programmers.co.kr/learn/courses/30/lessons/49191"""

from collections import defaultdict


def solution(num_boxer: int, results: list[list[int]]) -> int:
    fixed_ranker_count = 0

    winning_games = defaultdict(set)
    losing_games = defaultdict(set)

    for winner, loser in results:
        winning_games[winner].add(loser)

    visited_winners = [False] * (num_boxer + 1)

    def flatten_dependency(boxer_id: int):
        if visited_winners[boxer_id]:
            return winning_games[boxer_id]

        visited_winners[boxer_id] = True
        flatten_losers = set()
        for loser in winning_games[boxer_id]:
            losers = flatten_dependency(loser)
            flatten_losers.update(losers)

        flatten_losers.update(winning_games[boxer_id])

        return flatten_losers

    for boxer_id in range(1, num_boxer + 1):
        flatten_winning = flatten_dependency(boxer_id)

        winning_games[boxer_id].update(flatten_winning)
        for loser in flatten_winning:
            losing_games[loser].add(boxer_id)

    for boxer_id in range(1, num_boxer + 1):
        total_dependency = len(
            winning_games[boxer_id]) + len(losing_games[boxer_id])
        if total_dependency == num_boxer - 1:
            fixed_ranker_count += 1

    return fixed_ranker_count
