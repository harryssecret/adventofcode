def count_calories() -> list:
    elfs = []
    current_elf = 0

    with open("elf-data.txt", encoding="utf-8") as f:
        for line in f:
            if line == "\n":
                elfs.append(current_elf)
                current_elf = 0
            else:
                current_elf += int(line)
    return elfs


def strongest_elves(elves: list) -> int:
    sorted_strongest = sorted(elves, reverse=True)
    return sum(sorted_strongest[0:3])


elves = count_calories()
print(strongest_elves(elves))
