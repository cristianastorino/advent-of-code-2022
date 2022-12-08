def read_content(input: str) -> list[list[int]]:
    with open(input) as f:
        return [[int(tree) for tree in line.strip()] for line in f.readlines()]

def is_visible(trees: list[list[int]], x: int, y: int) -> bool:
    if x == 0 or y == 0 or x == len(trees)-1 or y == len(trees)-1:
        return True
    curr_tree_height = trees[y][x]
    row = trees[y]
    column = [row[x] for row in trees]
    if max(row[:x]) < curr_tree_height:
        return True
    if max(row[x+1:]) < curr_tree_height:
        return True
    if max(column[:y]) < curr_tree_height:
        return True
    if max(column[y+1:]) < curr_tree_height:
        return True
    return False

def part1(trees: list[list[int]]) -> int:
    return sum(is_visible(trees, x, y) for x in range(len(trees)) for y in range(len(trees)))

assert part1(read_content("day08-small.txt")) == 21
print(f"Part 1:\t{part1(read_content('day08.txt'))}")

def calc_scenic_score(trees: list[list[int]], x: int, y: int) -> int:
    if x == 0 or y == 0 or x == len(trees)-1 or y == len(trees)-1:
        return 0
    row = trees[y]
    column = [row[x] for row in trees]
    curr_tree_height = trees[y][x]
    left, right, up, down = 0, 0, 0, 0
    for tree in row[x-1::-1]:
        left += 1
        if tree >= curr_tree_height:
            break
    for tree in row[x+1:]:
        right += 1
        if tree >= curr_tree_height:
            break
    for tree in column[y-1::-1]:
        up += 1
        if tree >= curr_tree_height:
            break
    for tree in column[y+1:]:
        down += 1
        if tree >= curr_tree_height:
            break
    return left * right * up * down

def part2(trees: list[list[int]]) -> int:
    return max([calc_scenic_score(trees, x, y) for x in range(len(trees)) for y in range(len(trees))])

assert part2(read_content("day08-small.txt")) == 8
print(f"Part 2:\t{part2(read_content('day08.txt'))}")
