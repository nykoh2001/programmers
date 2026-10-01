# 3:07 ~ 3:23

def solution(park, routes):
    curr_x, curr_y = None, None
    obstacles = set()

    for row_idx, row in enumerate(park):
        for loc_idx, loc in enumerate(row):
            if loc == "S":
                curr_x = row_idx
                curr_y = loc_idx
                continue

            if loc == "X":
                obstacles.add((row_idx, loc_idx))
                continue

    DIRECTION_MAP = {
        "E": (0, 1),
        "W": (0, -1),
        "N": (-1, 0),
        "S": (1, 0)
    }

    row_count = len(park)
    col_count = len(park[0])

    def _is_valid_loc(x: int, y: int) -> bool:
        if x not in range(row_count) or y not in range(col_count):
            return False
        if (x, y) in obstacles:
            return False

        return True

    for route in routes:
        direction, distance_str = route.split()
        distance = int(distance_str)

        dx, dy = DIRECTION_MAP[direction]
        is_valid_loc = True
        for i in range(1, distance + 1):
            new_x = curr_x + dx * i
            new_y = curr_y + dy * i
            if not _is_valid_loc(new_x, new_y):
                is_valid_loc = False
                break

        if is_valid_loc:
            curr_x = curr_x + dx * distance
            curr_y = curr_y + dy * distance

    return [curr_x, curr_y]
