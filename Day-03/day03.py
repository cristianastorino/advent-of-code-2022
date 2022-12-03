def read_content(input: str) -> list[str]:
    with open(input) as f:
        return [line.strip() for line in f.readlines()]

def find_shared_item(line: str) -> str:
    first_half = line[:len(line)//2]
    second_half = line[len(line)//2:]
    return set(first_half).intersection(second_half).pop()

def calc_priority(item: str) -> int:
    return ord(item) - ord('A') + 27 if item.isupper() else ord(item) - ord('a') + 1

def part1(parsed_input: str) -> int:
    return sum(calc_priority(find_shared_item(line)) for line in parsed_input)

assert part1(read_content("day03-small.txt")) == 157
print(f"Part 1:\t{part1(read_content('day03.txt'))}")

def find_shared_items(parsed_input: str) -> list[str]:
    return [
        set(parsed_input[i]).intersection(set(parsed_input[i+1])).intersection(set(parsed_input[i+2])).pop() 
        for i in range(0, len(parsed_input), 3)
    ]

def part2(parsed_input: str) -> int:
    return sum(calc_priority(item) for item in find_shared_items(parsed_input))

assert part2(read_content("day03-small.txt")) == 70
print(f"Part 2:\t{part2(read_content('day03.txt'))}")
