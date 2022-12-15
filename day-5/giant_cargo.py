class GiantCargo:
    def __init__(self) -> None:
        self.lines = []

    def read_data_from_file(self, filename: str):
        with open(filename) as f:
            for line in f:
                if line == "\n":
                    break
                self.lines.append(line.replace("\n", ""))

    def parse_cargo(self) -> None:
        parsed_lines = []
        for l in self.lines:
            actual_line = []
            for i in range(1, len(l), 4):
                actual_line.append(l[i])
            parsed_lines.append(actual_line)
        self.cargo = parsed_lines
        self.size = len(parsed_lines[-1])

    def new_line(self):
        self.cargo.insert(0, ['' * self.size])

    def move_crate(self, number: int, from_i: int, to_i: int) -> None:
        for i in range(number):
            current_list = self.cargo[i]
            if self.isCrateHere(i, to_i):
                pass
            self.cargo[i] = current_list
        pass

    def isCrateHere(self, deep: int, position: int) -> bool:
        return self.cargo[deep][position] != ' '

    def show(self):
        for l in self.cargo:
            print(l)


class Crate:
    def __init__(self, letter: str) -> None:
        self.name = letter
