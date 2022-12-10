def read_content(input: str) -> list[str]:
    with open(input) as f:
        return [line.strip() for line in f.readlines()]

def parse_operation(line: str) -> tuple[int, int]:
    match line:
        case "noop":
            cycle = 1
            inc = 0
        case _:
            cycle = 2
            inc = int(line.split()[-1])
    return cycle, inc

def calc_signal_strengths(operations: list[tuple[int, int]]) -> list[int]:
    signal_strengths = []
    x_register_value = 1
    cycle_number = 1
    for op in operations:
        cycle, inc = op
        for _ in range(cycle):
            if cycle_number % 40 == 20:
                signal_strengths.append(x_register_value * cycle_number)
            cycle_number += 1
        x_register_value += inc
    return signal_strengths

def part1(lines: list[str]) -> int:
    return sum(calc_signal_strengths(map(parse_operation, lines)))

assert part1(read_content("day10-small.txt")) == 13140
print(f"Part 1:\t{part1(read_content('day10.txt'))}")

def calc_crt_screen(operations: list[tuple[int, int]]) -> list[int]:
    crt_screen = []
    x_register_value = 1
    for op in operations:
        cycle, inc = op
        for _ in range(cycle):
            crt_screen.append("#" if len(crt_screen) % 40 in range(x_register_value-1, x_register_value+2) else ".")
        x_register_value += inc
    return crt_screen        

def part2(lines: list[str]):
    crt_screen = calc_crt_screen(map(parse_operation, lines))
    print("Part 2:")
    print(''.join(crt_screen[:40]))
    print(''.join(crt_screen[40:80]))
    print(''.join(crt_screen[80:120]))
    print(''.join(crt_screen[120:160]))
    print(''.join(crt_screen[160:200]))
    print(''.join(crt_screen[200:]))

part2(read_content('day10.txt'))
