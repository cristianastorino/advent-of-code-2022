from copy import deepcopy

def read_content(input: str) -> list[str]:
    with open(input) as f:
        return f.read().split("\n\n")

def parse_stacks(lines: list[str]) -> list[list[str]]:
    stacks = []
    for crate in lines[-1].split():
        stacks.append([])
    for line in lines[:-1]:
        for i in range(len(stacks)):
            crate = line[i*4+1]
            if crate != " ":
                stacks[i].append(crate)
    return stacks

def rearrange(moves: list[str], stacks: list[list[str]]) -> list[list[str]]:
    new_stacks = deepcopy(stacks)
    for line in moves:
        command = line.split(" ")
        qty = int(command[1])
        src = int(command[3]) - 1
        dst = int(command[5]) - 1
        new_stacks[dst] = [*reversed(new_stacks[src][:qty]), *new_stacks[dst]]
        new_stacks[src] = new_stacks[src][qty:]
    return new_stacks

def part1(input: str) -> str:
    stacks, moves = read_content(input)
    stacks = parse_stacks(stacks.splitlines())
    stacks = rearrange(moves.splitlines(), stacks)
    return "".join([stack[0] for stack in stacks])

assert part1("day05-small.txt") == "CMZ"
print(f"Part 1:\t{part1('day05.txt')}")

def rearrange_same_order(moves: list[str], stacks: list[list[str]]) -> list[list[str]]:
    new_stacks = deepcopy(stacks)
    for line in moves:
        command = line.split(" ")
        qty = int(command[1])
        src = int(command[3]) - 1
        dst = int(command[5]) - 1
        new_stacks[dst] = [*new_stacks[src][:qty], *new_stacks[dst]]
        new_stacks[src] = new_stacks[src][qty:]
    return new_stacks

def part2(input: str) -> str:
    stacks, moves = read_content(input)
    stacks = parse_stacks(stacks.splitlines())
    stacks = rearrange_same_order(moves.splitlines(), stacks)
    return "".join([stack[0] for stack in stacks])

assert part2("day05-small.txt") == "MCD"
print(f"Part 2:\t{part2('day05.txt')}")
