class GiantCargo:
    def read_data_from_file(self, filename: str):
        print("aa")
        with open(filename) as f:
            for line in f:
                if line == "\n":
                    print("WAAAA")

    def parse_cargo(self):
        lines = []
        for line in self.read_data_from_file():
            pass


class Crate:
    def __init__(self) -> None:
        pass
