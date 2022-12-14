def read_content(input: str) -> list[str]:
    with open(input) as f:
        return [line.strip() for line in f.readlines()]

def get_points_between(p1: tuple[int, int], p2: tuple[int, int]) -> set[tuple[int, int]]:
    x1, y1 = p1
    x2, y2 = p2
    points_between = set()
    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            points_between.add((x, y1))
    elif x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            points_between.add((x1, y))
    return points_between

def parse_lines(lines: list[str]) -> set[tuple[int, int]]:
    parsed_lines = set()
    for line in lines:
        points = line.split("->")
        for i in range(len(points) - 1):
            p1 = map(int, points[i].strip().split(","))
            p2 = map(int, points[i + 1].strip().split(","))
            parsed_lines = parsed_lines.union(get_points_between(p1, p2))
    return parsed_lines

def get_sand_moves_rules(x: int, y: int) -> list[tuple[int, int]]:
    return [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]

def calc_falling_sand(lines: list[str], bottomless: bool) -> int:
    initial_position = (500, 0)
    lines = parse_lines(lines)
    bottom = max(y for (_, y) in lines) + (0 if bottomless else 2)
    blocked_sand = set()
    current_sand = initial_position
    while True:
        move_1, move_2, move_3 = get_sand_moves_rules(*current_sand)
        if not bottomless and move_1[1] == bottom:
            blocked_sand.add(current_sand)
            current_sand = initial_position
        elif move_1 not in lines and move_1 not in blocked_sand:
            current_sand = move_1
        elif move_2 not in lines and move_2 not in blocked_sand:
            current_sand = move_2
        elif move_3 not in lines and move_3 not in blocked_sand:
            current_sand = move_3
        else:
            blocked_sand.add(current_sand)
            if current_sand == initial_position:
                break
            current_sand = initial_position
        if current_sand[1] == bottom:
            break
    return len(blocked_sand)

def part1(input: str) -> int:
    return calc_falling_sand(read_content(input), True)

assert part1("day14-small.txt") == 24
print(f"Part 1:\t{part1('day14.txt')}")

def part2(input: str) -> int:
    return calc_falling_sand(read_content(input), False)

assert part2("day14-small.txt") == 93
print(f"Part 2:\t{part2('day14.txt')}")
