def calc_calories(input: str) -> list[int]:
    with open(input) as f:
        return [sum(int(cal) for cal in elf.split()) for elf in f.read().split("\n\n")]

def calc_max(cals: list[int]) -> int:
    return max(cals)

def calc_max_top_three(cals: list[int]) -> int:
    return sum(sorted(cals)[-3:])

# example input
calories_small = calc_calories("day01-small.txt")
max_small = calc_max(calories_small)
assert max_small == 24000
top_three_small = calc_max_top_three(calories_small)
assert top_three_small == 45000

# puzzle input
calories = calc_calories("day01.txt")
print(f"Part 1:\t{calc_max(calories)}")
print(f"Part 2:\t{calc_max_top_three(calories)}")