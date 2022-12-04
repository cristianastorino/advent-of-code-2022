def read_content(input: str) -> list[str]:
    with open(input) as f:
        return [line.strip() for line in f.readlines()]

def calc_assignments(line: str) -> tuple[str, str]:
    splitted = line.split(',')
    return (splitted[0], splitted[1])

def calc_sections(sections: str) -> list[int]:
    splitted = sections.split('-')
    return range(int(splitted[0]), int(splitted[1])+1)

def fully_contains(first_pair: list[int], second_pair: list[int]) -> bool:
    return set(first_pair).issubset(second_pair) or set(second_pair).issubset(first_pair)

def part1(parsed_input: str) -> int:
    return sum(
        fully_contains(calc_sections(calc_assignments(line)[0]), calc_sections(calc_assignments(line)[1]))
        for line in parsed_input
    )

assert part1(read_content("day04-small.txt")) == 2
print(f"Part 1:\t{part1(read_content('day04.txt'))}")

def are_overlapping(first_pair: list[int], second_pair: list[int]) -> bool:
    return len(set(first_pair).intersection(second_pair)) > 0

def part2(parsed_input: str) -> int:
    return sum(
        are_overlapping(calc_sections(calc_assignments(line)[0]), calc_sections(calc_assignments(line)[1]))
        for line in parsed_input
    )

assert part2(read_content("day04-small.txt")) == 4
print(f"Part 2:\t{part2(read_content('day04.txt'))}")
