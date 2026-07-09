"""https://school.programmers.co.kr/learn/courses/30/lessons/468370"""

from collections import Counter


def solution(message, spoiler_ranges):
    real_message_idx = 0
    spoiler_word_counter = Counter()
    unspoiler_word_set = set()

    len_message = len(message)
    len_spoiler_words = len(spoiler_ranges)
    spoiler_word_idx = 0
    current_spoiler_range = spoiler_ranges[spoiler_word_idx]

    word_start_idx, word_end_idx = None, None
    for i in range(len(message)):
        if i < real_message_idx or (word_start_idx is None and message[i] == " "):
            continue
        if word_start_idx is None and message[i] != " ":
            word_start_idx = i
            # print(f"Start of word: {(word_start_idx, word_end_idx)}")

        # Handle spoiler word that corresponds to current range
        spoiler_start, spoiler_end = current_spoiler_range
        # print(f"Current Spoiler Range: {current_spoiler_range}")
        # print(f"Current Spoiler Idx: {spoiler_word_idx}")

        if i > spoiler_end:
            if spoiler_word_idx >= len_spoiler_words - 1:
                spoiler_start = len_message + 1
                spoiler_end = spoiler_start
            else:
                spoiler_word_idx += 1
                current_spoiler_range = spoiler_ranges[spoiler_word_idx]
                spoiler_start, spoiler_end = current_spoiler_range

        # If it is spoiler word
        if i >= spoiler_start and i <= spoiler_end:
            if word_start_idx is None and message[i] == " ":
                word_start_idx = i + 1
                i += 1
                real_message_idx = i

            while i < len_message and message[i] != " ":
                i += 1

            word_end_idx = i
            real_message_idx = i + 1
            # print(f"End of word: {(word_start_idx, word_end_idx)}")

            spoiler_part = message[word_start_idx:word_end_idx]
            spoiler_words = spoiler_part.split()
            spoiler_word_counter.update(spoiler_words)
            word_start_idx, word_end_idx = None, None

        # If the word is end without spoiler part
        elif message[i] == " " or i == len_message - 1:
            word_end_idx = i + 1
            # print(f"End of word: {(word_start_idx, word_end_idx)}")

            unspoiled_part = message[word_start_idx:word_end_idx]
            unspoiled_words = unspoiled_part.split()

            unspoiler_word_set.update(unspoiled_words)
            word_start_idx, word_end_idx = None, None

        # print(spoiler_word_counter)
        # print(unspoiler_word_set)

    spoiler_word_count = 0
    for spoiler_candidate, frequency in spoiler_word_counter.items():
        if frequency != 1 or spoiler_candidate in unspoiler_word_set:
            continue
        spoiler_word_count += 1

    return spoiler_word_count


if __name__ == "__main__":
    print(
        solution(
            "my phone number is 01012345678 and may i have your phone number",
            [[5, 5], [25, 28], [34, 40], [53, 59]],
        )
    )
