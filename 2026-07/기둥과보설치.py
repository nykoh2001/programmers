def solution(n: int, build_frame: list[list[int]]) -> list[list[int]]:
    structure = set()

    def is_valid(x: int, y: int, structure_type: int) -> bool:
        # 기둥
        if structure_type == 0:
            return (
                y == 0
                or (x - 1, y, 1) in structure
                or (x, y, 1) in structure
                or (x, y - 1, 0) in structure
            )

        # 보
        return (
            (x, y - 1, 0) in structure
            or (x + 1, y - 1, 0) in structure
            or (
                (x - 1, y, 1) in structure
                and (x + 1, y, 1) in structure
            )
        )

    for x, y, structure_type, command in build_frame:
        # print(f"structue: {structure}")
        # print(f"{x}, {y}, {a}, {b}")
        if command == 1:
            structure.add((x, y, structure_type))
            if all(is_valid(c_x, c_y, c_st) for c_x, c_y, c_st in structure):
                continue
            structure.remove((x, y, structure_type))

        else:  # command == 0, 삭제
            if (x, y, structure_type) not in structure:
                continue
            structure.remove((x, y, structure_type))
            if all(is_valid(c_x, c_y, c_st) for c_x, c_y, c_st in structure):
                continue
            structure.add((x, y, structure_type))

    return sorted(list(structure))
