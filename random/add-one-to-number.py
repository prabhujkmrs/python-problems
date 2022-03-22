"""Add one to number"""


def solution(arr: list) -> int:
    size = len(arr)
    index = size - 1

    while index >= 0:
        if sum(arr[index]) < 10:
            arr[index] = arr[index] + 1
            break
        else:
            arr[index] = 0
            index -= 1

    if sum(arr[0]) == 1:
        arr.insert(0, 1)

    return arr


def sum(val):
    return val + 1


print(solution([9, 9, 3]))
