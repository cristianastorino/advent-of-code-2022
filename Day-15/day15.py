import re

def read_content(input: str) -> list[str]:
    with open(input) as f:
        return [line.strip() for line in f.readlines()]

def calc_manhattan_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x2 - x1) + abs(y2 - y1)

def calc_row_intersections(x: int, y: int, radius: int, row_number: int) -> list[tuple[int, int]]:
    intersection = []
    if calc_manhattan_distance(x, y, x, row_number) <= radius:
        intersection.append((x, row_number))
    left = x - 1 # move versus left
    right = x + 1 # move versus right
    while True:
        left_valid = calc_manhattan_distance(x, y, left, row_number) <= radius
        if left_valid:
            intersection.append((left, row_number))
        right_valid = calc_manhattan_distance(x, y, right, row_number) <= radius
        if right_valid:
            intersection.append((right, row_number))
        if left_valid or right_valid:
            left = left - 1 # continue
            right = right + 1 # continue
        else:
            break
    return intersection

def part1(lines: list[str], row_number: int) -> int:
    magic_pattern = re.compile(r".=(-?\d+)")
    beacons_found = []
    row_in_radius = []
    sensors = []
    for line in lines:
        sx, sy, bx, by = [int(s) for s in magic_pattern.findall(line)]
        radius = calc_manhattan_distance(sx, sy, bx, by)
        sensors.append(((sx, sy), radius))
        if by == row_number:
            beacons_found.append((bx, by))
        row_in_radius.append(calc_row_intersections(sx, sy, radius, row_number))
    return len(set(sum(row_in_radius, [])).difference(beacons_found))

assert part1(read_content("day15-small.txt"), 10) == 26
print(f"Part 1:\t{part1(read_content('day15.txt'), 2000000)}")

def calc_perimeter(x: int, y: int, radius: int, max_coord: int) -> list[tuple[int, int]]:
    perimeter_radius = radius + 1
    perimeter = []
    min_y = max(y - perimeter_radius, 0)
    max_y = min(y + perimeter_radius, max_coord)
    for py in range(min_y, max_y + 1):
        distance_remaining = perimeter_radius - abs(y - py)
        if x + distance_remaining <= max_coord:
            perimeter.append((x + distance_remaining, py))
        if x - distance_remaining >= 0:
            perimeter.append((x - distance_remaining, py))
    return perimeter

def find_unreachable(lines: list[str], max_coordinate: int) -> tuple[int, int]:
    magic_pattern = re.compile(r".=(-?\d+)")
    sensors = []
    for line in lines:
        sx, sy, bx, by = [int(s) for s in magic_pattern.findall(line)]
        radius = calc_manhattan_distance(sx, sy, bx, by)
        sensors.append(((sx, sy), radius))
    for (sx, sy), radius in sensors:
        perimeter = calc_perimeter(sx, sy, radius, max_coordinate)
        for (px, py) in perimeter:
            reachable = False
            for (sx, sy), radius in sensors:
                if calc_manhattan_distance(px, py, sx, sy) <= radius:
                    reachable = True
                    break
            if not reachable:
                return (px, py)
    raise ValueError("🎄")

def part2(lines: list[str], max_coordinate: int) -> int:
    bx, by = find_unreachable(lines, max_coordinate)
    return 4000000 * bx + by

assert part2(read_content("day15-small.txt"), 20) == 56000011
print(f"Part 2:\t{part2(read_content('day15.txt'), 4000000)}")