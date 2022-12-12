from collections import deque
import string
import sys

def read_content(input: str) -> list[str]:
    with open(input) as f:
        return [line.strip() for line in f.readlines()]

def is_inside_area(area: list[str], row: int, col: int):
    return row >= 0 and col >= 0 and col < len(area[0]) and row < len(area)

def calc_start(area: list[str]) -> tuple[int, int]:
    for row in range(len(area)):
        for col in range(len(area[0])):
            if area[row][col] == 'S':
                return row, col

def calc_min_path_len(area: list[str], row: int, col: int) -> int:
    elevations = {character: index for index, character in enumerate(string.ascii_lowercase)}
    elevations['S'] = 0
    elevations['E'] = 25
    step = 0
    steps = []
    visited = set()
    nodes = deque([(row, col, None, step)])
    while nodes:
        row, col, previous, step = nodes.popleft()
        if not is_inside_area(area, row, col) or (row, col) in visited:
            continue
        curr = area[row][col]
        if previous is not None and elevations[curr] > elevations[previous] + 1:
            continue
        if area[row][col] == 'E':
            steps.append(step)
            continue
        nodes.append((row + 1, col, curr, step + 1))
        nodes.append((row - 1, col, curr, step + 1))
        nodes.append((row, col + 1, curr, step + 1))
        nodes.append((row, col - 1, curr, step + 1))
        visited.add((row, col))
    return min(steps) if (len(steps) > 0) else sys.maxsize

def part1(input: str) -> int:
    area = read_content(input)
    return calc_min_path_len(area, *calc_start(area))

assert part1("day12-small.txt") == 31
print(f"Part 1:\t{part1('day12.txt')}")

def calc_all_starts(area: list[str]) -> list[tuple]:
    return [
        (row, col)
        for row in range(len(area))
        for col in range(len(area[0]))
        if area[row][col] in 'aS'
    ]

def part2(input: str) -> int:
    area = read_content(input)
    return min(calc_min_path_len(area, row, col) for row, col in calc_all_starts(area))

assert part2("day12-small.txt") == 29
print(f"Part 2:\t{part2('day12.txt')}")