# https://school.programmers.co.kr/learn/courses/30/lessons/43163
# 2:04 ~ 2:14
# 인접한 단어 == 철자 하나만 다른 단어

from collections import defaultdict, deque

def solution(begin: str, target: str, words: list[str]) -> int:
    word_graph = defaultdict(list)
    
    if target not in words:
        return 0
    
    def _find_word_variations(curr_word: str) -> list[str]:
        variations = []
        for word in words:
            diff_count = 0
            for c1, c2 in zip(curr_word, word):
                if c1 != c2:
                    diff_count += 1
            
            if diff_count == 1:
                variations.append(word)
        return variations

    word_graph[begin] = _find_word_variations(begin)
    for word in words:
        word_graph[word] = _find_word_variations(word)
    
    visited_word = set([begin])
    words_to_visit = deque([(begin, 0)])
    while words_to_visit:
        curr_word, curr_cost = words_to_visit.popleft()
        for variation in word_graph[curr_word]:
            if variation in visited_word:
                continue
            
            if variation == target:
                return curr_cost + 1
            words_to_visit.append((variation, curr_cost + 1))
            visited_word.add(variation)
    
    return 0
    