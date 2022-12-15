from giant_cargo import GiantCargo


def main() -> None:
    cargo = GiantCargo()
    cargo.read_data_from_file("test_data.txt")
    cargo.parse_cargo()
    cargo.show()


if __name__ == "__main__":
    main()
