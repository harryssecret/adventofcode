from giant_cargo import GiantCargo


def main() -> None:
    cargo = GiantCargo()
    cargo.read_data_from_file("puzzle.txt")


if __name__ == "__main__":
    main()
