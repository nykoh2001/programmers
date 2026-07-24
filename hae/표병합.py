from collections import defaultdict

TABLE_MAX_IDX = 51


def _update_all_value(
    table: list[list[int]], value1: str, value2: str, merge_state: dict
) -> None:
    for row_idx in range(1, TABLE_MAX_IDX):
        for col_idx in range(1, TABLE_MAX_IDX):
            if table[row_idx][col_idx] == value1:
                table[row_idx][col_idx] = value2
                for merged_r, merged_c in merge_state[(row_idx, col_idx)]:
                    table[merged_r][merged_c] = value2


def solution(commands):
    print_results = []

    table = [[""] * TABLE_MAX_IDX for _ in range(TABLE_MAX_IDX)]
    merge_state = defaultdict(set)

    for command in commands:
        command_splits = command.split()
        command_type, command_args = command_splits[0], command_splits[1:]

        if command_type == "UPDATE":
            len_args = len(command_args)
            if len_args == 2:
                value1, value2 = command_args
                _update_all_value(table, value1, value2, merge_state)
                continue

            # len_args == 3:
            r_str, c_str, value = command_args
            r, c = int(r_str), int(c_str)
            table[r][c] = value
            for merged_r, merged_c in merge_state[(r, c)]:
                table[merged_r][merged_c] = value
            continue

        if command_type == "MERGE":
            r1, c1, r2, c2 = list(map(int, command_args))
            if r1 == r2 and c1 == c2:
                continue

            merge_state[(r1, c1)].add((r1, c1))
            merge_state[(r1, c1)].add((r2, c2))
            merge_state[(r1, c1)].update(merge_state[(r2, c2)])
            for r, c in merge_state[(r1, c1)]:
                merge_state[(r, c)].update(merge_state[(r1, c1)])

            if table[r1][c1]:
                for merged_r, merged_c in merge_state[(r1, c1)]:
                    table[merged_r][merged_c] = table[r1][c1]
                continue

            if table[r2][c2]:
                for merged_r, merged_c in merge_state[(r2, c2)]:
                    table[merged_r][merged_c] = table[r2][c2]
                continue

        if command_type == "UNMERGE":
            r, c = list(map(int, command_args))
            for merged_r, merged_c in merge_state[(r, c)]:
                if r == merged_r and c == merged_c:
                    continue

                merge_state.pop((merged_r, merged_c))
                table[merged_r][merged_c] = ""
            merge_state.pop((r, c))
            continue

        if command_type == "PRINT":
            r, c = list(map(int, command_args))
            print_results.append(table[r][c] if table[r][c] else "EMPTY")
            continue

    return print_results
