def read_content(input: str) -> list[str]:
    with open(input) as f:
        return [line.strip() for line in f.readlines()]

def parse_motion(dir: str, steps: str) -> tuple[str, int]:
    return dir, int(steps)

def parse_motions(lines: list[str]) -> list[tuple[str, int]]:
    return [parse_motion(*line.split()) for line in lines]

DIRS = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1)
}

def sign(x: int) -> int:
    return (x > 0) - (x < 0)

def visit(number_of_knots: int, motions: list[tuple[str, int]]) -> int:
    knots = [(0, 0)] * number_of_knots
    seen = {(0, 0)}
    for move, steps in motions:
        for _ in range(steps):
            x, y = knots[0]
            dx, dy = DIRS[move]
            knots[0] = (x + dx, y + dy)
            for i in range(number_of_knots - 1):
                x, y = knots[i]
                tx, ty = knots[i + 1]
                dx, dy = x - tx, y - ty
                if dx**2 + dy**2 >= 4:
                    knots[i + 1] = (tx + sign(dx), ty + sign(dy))
            seen.add(knots[number_of_knots-1])
    return len(seen)

def part1(input: str) -> int:
    return visit(2, parse_motions(read_content(input)))

assert part1("day09-small.txt") == 13
print(f"Part 1:\t{part1('day09.txt')}")

def part2(input: str) -> int:
    return visit(10, parse_motions(read_content(input)))

assert part2("day09-small.txt") == 1
print(f"Part 2:\t{part2('day09.txt')}")