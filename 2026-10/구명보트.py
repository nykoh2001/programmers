# 3:24 ~ 3:35

def solution(people, limit):
    people.sort(reverse=True)
    boat_count = 0

    left, right = 0, len(people) - 1
    while left <= right:
        if people[left] + people[right] <= limit:
            boat_count += 1
            left += 1
            right -= 1
            continue

        boat_count += 1
        left += 1

    return boat_count
