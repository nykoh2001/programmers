from itertools import combinations_with_replacement as cwr
from collections import defaultdict
import heapq as hq


def solution(k: int, n: int, reqs: list[list[int]]) -> int:
    meeting_type_list = [mt for mt in range(1, k + 1)]
    assignment_list = cwr(meeting_type_list, n - k)

    min_latency = 10 ** 9
    for assignment in assignment_list:
        latency = 0
        assignment_dict = {mt: 1 for mt in meeting_type_list}
        for meeting_type in assignment:
            assignment_dict[meeting_type] += 1

        meeting_end_by_type = {
            mt: [0] * num_counseller for mt, num_counseller in assignment_dict.items()
        }

        for start, duration, meeting_type in reqs:
            end = start + duration
            meeting_end = meeting_end_by_type[meeting_type][0]

            current_latency = max(meeting_end - start, 0)
            latency += current_latency

            hq.heappop(meeting_end_by_type[meeting_type])
            hq.heappush(
                meeting_end_by_type[meeting_type], end + current_latency)

        min_latency = min(min_latency, latency)

    return min_latency
