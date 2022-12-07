def read_content(input: str) -> list[str]:
    with open(input) as f:
        return [line.strip() for line in f.readlines()]

def parse_dir_tree(content: list[str]) -> dict[str, int]:
    dir_tree = {}
    current_dir = []
    for line in content:
        splitted = line.split()
        if splitted[0] == "$":
            if splitted[1] == "cd":
                if splitted[2] == "..":
                    current_dir.pop()
                else:
                    path = '/' if splitted[2] == '/' else current_dir[-1] + '/' + splitted[2]
                    current_dir.append(path)
                    dir_tree[path] = 0
        elif splitted[0] != "dir":
                for d in current_dir:
                    dir_tree[d] += int(splitted[0])
    return dir_tree

def part1(input: str) -> int:
    dir = parse_dir_tree(input)
    return sum(dir[d] for d in dir if dir[d] <= 100000)

assert part1(read_content("day07-small.txt")) == 95437
print(f"Part 1:\t{part1(read_content('day07.txt'))}")

def part2(input: str) -> int:
    dir = parse_dir_tree(input)
    target = dir['/'] - 40000000 # (70000000-30000000=40000000)
    return min([dir[d] for d in dir if dir[d] > target])

assert part2(read_content("day07-small.txt")) == 24933642
print(f"Part 2:\t{part2(read_content('day07.txt'))}")
