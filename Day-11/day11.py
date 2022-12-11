import re
from math import floor, lcm, prod
from copy import deepcopy

def read_content(input: str) -> str:
    with open(input) as f:
        return f.read()

def parse_monkeys(input: str) -> list[dict]:    
    items = [[int(val.strip()) for val in it.split(",")] for it in re.findall(r"Starting items: ((?:\d+,?\s?)*)", input)]
    operations = re.findall(r"Operation: new = (.*)?", input)
    divisors = [int(val) for val in re.findall(r"divisible by (\d+)?", input)]
    actions = [(int(t), int(f)) for t, f in re.findall(r"If true: throw to monkey (\d+)\n\s+If false: throw to monkey (\d+)", input)]
    monkeys = []
    for i in range(len(input.split("\n\n"))):
        monkeys.append({
            "items": items[i],
            "operation": operations[i],
            "divisor": divisors[i],
            "action": actions[i],
            "inspected": 0
        })
    return monkeys

def run_rounds(monkeys: list[dict], number_of_rounds: int, lcm_value: int, divide: bool) -> list[dict]:
    new_monkeys = deepcopy(monkeys)
    for _ in range(number_of_rounds):
        for m in new_monkeys:
            for old in m["items"]:
                new_worry_level = floor(eval(m["operation"]) / 3) if divide else eval(m["operation"])
                dest = m["action"][bool(new_worry_level % m["divisor"])]
                new_monkeys[dest]["items"].append(new_worry_level % lcm_value)
            m["inspected"] += len(m["items"])
            m["items"] = []
    return new_monkeys

def solve(monkeys: list[dict], number_of_rounds: int, divide: bool) -> int:
    lcm_value = lcm(*[m["divisor"] for m in monkeys])
    new_monkeys = run_rounds(monkeys, number_of_rounds, lcm_value, divide)
    return prod(sorted([m["inspected"] for m in new_monkeys])[-2:])

def part1(input: str) -> int:
    return solve(parse_monkeys(input), 20, True)

assert part1(read_content("day11-small.txt")) == 10605
print(f"Part 1:\t{part1(read_content('day11.txt'))}")

def part2(input: str) -> int:
    return solve(parse_monkeys(input), 10000, False)

assert part2(read_content("day11-small.txt")) == 2713310158
print(f"Part 2:\t{part2(read_content('day11.txt'))}")
