import string

def parse_input(filename: str):
    with open(filename) as f:
        for line in f:
            yield line

def find_item_priority(item: str):
    return string.ascii_letters.find(item) + 1
    
def main() -> None:
    final_priority = 0
    for rucksack in find_good_rucksack('puzzle.txt'):
            mistake = find_mistake(rucksack)
            final_priority += find_item_priority(mistake)
    print(final_priority)

def find_good_rucksack(filename: str):
    for rucksack in parse_input(filename):
            rucksack = rucksack.replace("\n", "")
            if len(rucksack) % 2 == 0:
                yield rucksack


def find_mistake(rucksack: str):
    half_size = int(len(rucksack) / 2)
    first_half = rucksack[:half_size]
    second_half = rucksack[half_size:]
    for char in first_half:
        if second_half.find(char) != -1:
            return char

if __name__ == "__main__":
    main()
