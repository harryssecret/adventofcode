from typing import List


def read_file(filename: str) -> str:
    with open(filename) as f:
        for line in f:
            yield line.replace("\n", "")


def find_sections(line: str) -> List[List[int]]:
    groups = line.split(",")
    result = []
    for group in groups:
        section = []
        for digit in group.split("-"):
            section.append(int(digit))
        result.append(section)
    return result


def does_fully_contains(section: List[List[int]]) -> bool:
    first_section, second_section = section
    return (is_between(second_section[0], first_section[0], first_section[1]) and is_between(second_section[1], first_section[0], first_section[1])) or (is_between(
        first_section[0], second_section[0], second_section[1]) and is_between(first_section[1], second_section[0], second_section[1]))


def is_overlap(section: List[List[int]]) -> bool:
    first_section, second_section = section
    if first_section[0] <= second_section[0] <= first_section[1] or second_section[0] <= first_section[0] <= second_section[1]:
        return True
    return False


def is_between(number_to_check: int, lowest_number: int, biggest_number: int) -> bool:
    return lowest_number <= number_to_check <= biggest_number


def count_contained_numbers(filename: str) -> int:
    counter = 0
    for line in read_file(filename):
        section = find_sections(line)
        if does_fully_contains(section):
            counter += 1
    return counter


def count_overlapping_numbers(filename: str) -> int:
    count = 0
    for line in read_file(filename):
        section = find_sections(line)
        print(section, is_overlap(section))
        if is_overlap(section):
            count += 1
    return count


def main():
    filename = "puzzle.txt"
    number_overlaps = count_contained_numbers(filename)
    print(number_overlaps)
    print(count_overlapping_numbers(filename))


if __name__ == '__main__':
    main()
