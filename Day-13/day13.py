def read_content(input: str) -> list[str]:
    with open(input) as f:
        return [line.strip() for line in f.readlines()]

class Node:
    def __init__(self, value = None):
        self.value: int = value
        self.children: list[Node] = []

    def is_leaf(self):
        return self.value is not None

    def add_child(self, child):
        self.children.append(child)

    @staticmethod
    def from_input(input: str) -> "Node":
        return Node.from_list_int(eval(input))

    @staticmethod
    def from_list_int(list_input: list) -> "Node":
        res = Node()
        for item in list_input:
            if type(item) is int:
                res.add_child(Node(item))
            else:
                res.add_child(Node.from_list_int(item))
        return res

    def __repr__(self) -> str:
        if self.value is not None:
            return str(self.value)
        return "[" + ",".join((str(child) for child in self.children)) + "]"

    def compare(self, oth: "Node") -> int:
        if self.is_leaf() and oth.is_leaf():
            return self.value - oth.value
        if self.is_leaf():
            tmp = Node()
            tmp.add_child(self)
            return tmp.compare(oth)
        if oth.is_leaf():
            tmp = Node()
            tmp.add_child(oth)
            return self.compare(tmp)
        for node1, node2 in zip(self.children, oth.children):
            result = node1.compare(node2)
            if result != 0:
                return result
        return len(self.children) - len(oth.children)

    def __lt__(self, other: "Node") -> bool:
        return self.compare(other) < 0

def parse_packets(lines: list[str]) -> list[(Node, Node)]:
    packets: list[(Node, Node)] = []
    for i in range(len(lines) // 3 + 1):
        entry1 = lines[3*i]
        entry2 = lines[3*i + 1]
        packets.append((Node.from_input(entry1), Node.from_input(entry2)))
    return packets

def part1(input: str) -> int:
    lines = read_content(input)
    packets = parse_packets(lines)
    indices_sum = 0
    for i in range(len(packets)):
        node1, node2 = packets[i]
        if node1 < node2:
            indices_sum += i + 1 # first pair has index 1
    return indices_sum
    
assert part1("day13-small.txt") == 13
print(f"Part 1:\t{part1('day13.txt')}")

def part2(input: str) -> int:
    lines = read_content(input)
    packets = parse_packets(lines)
    add_divider_packet1 = Node.from_list_int([[2]])
    add_divider_packet2 = Node.from_list_int([[6]])    
    flattened_packets = [item for sublist in packets for item in sublist]
    flattened_packets.append(add_divider_packet1)
    flattened_packets.append(add_divider_packet2)
    flattened_packets.sort()    
    for i in range(len(flattened_packets)):
        if flattened_packets[i] == add_divider_packet1:
            first_packet = i + 1 # The first packet is at index 1
        elif flattened_packets[i] == add_divider_packet2:
            second_packet = i + 1 # The first packet is at index 1
            break
    return first_packet * second_packet
    
assert part2("day13-small.txt") == 140
print(f"Part 2:\t{part2('day13.txt')}")
