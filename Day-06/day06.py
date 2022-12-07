def read_content(input: str) -> str:
    with open(input) as f:
        return f.read().strip()

def find_start_packet_marker(input: str, nChars: int) -> int:
    for i in range(len(input)):
        tmp = input[i:i+nChars]
        if len(tmp) == len(set(tmp)):
            return i + nChars

def part1(input: str) -> int:
    return find_start_packet_marker(read_content(input), 4)

assert part1("day06-small.txt") == 7
print(f"Part 1:\t{part1('day06.txt')}")

def part2(input: str) -> int:
    return find_start_packet_marker(read_content(input), 14)

assert part2("day06-small.txt") == 19
print(f"Part 2:\t{part2('day06.txt')}")