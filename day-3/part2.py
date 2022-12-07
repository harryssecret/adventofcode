from main import format_rucksack, find_item_priority
from typing import List


def main():
    elves = create_elves_group('puzzle-input.txt')
    final_priority = 0
    for elves_group in elves:
        item = find_matching_char(elves_group)
        final_priority += find_item_priority(item)
    print(final_priority)


def create_elves_group(filename: str) -> list:
    elf_batch = []
    all_elves = []
    for rucksack in format_rucksack(filename):
        elf_batch.append(rucksack)
        if len(elf_batch) >= 3:
            all_elves.append(elf_batch)
            elf_batch = []
    return all_elves


def find_matching_char(group_list: List[List[str]]) -> str:
    for char in group_list[0]:
        for char2 in group_list[1]:
            for char3 in group_list[2]:
                if char == char2 == char3:
                    return char


if __name__ == "__main__":
    main()
