from argparse import ArgumentParser


def sort(width: float, height: float, length: float, mass: float) -> str:
    """Sort the package based on its dimensions and mass.
    --------------------------
    Parameters:
    width: float
        The width of the package.
    height: float
        The height of the package.
    length: float
        The length of the package.
    mass: float
        The mass of the package.
    --------------------------
    Returns:
    str
        The label of the package for sorting."""
    assert any([i > 0 for i in [width, height, length, mass]]
               ), "cannot compute on dimensions with negative or zero values."
    # avoid magic numbers by defining constants
    bulk_max = 1_000_000
    max_weight = 20
    # compute the volume
    volume = width * length * height
    # check if the package is bulky or heavy
    bulky = volume >= bulk_max
    heavy = mass >= max_weight
    # check if the package is rejected
    rejected = heavy and bulky
    label = "REJECTED" if rejected else "SPECIAL" if bulky or heavy \
        else "STANDARD"
    return label


def main():
    # test the function
    parser = ArgumentParser()
    parser.add_argument("--width", type=float, default=10)
    parser.add_argument("--height", type=float, default=10)
    parser.add_argument("--length", type=float, default=10)
    parser.add_argument("--mass", type=float, default=10)
    args = parser.parse_args()
    label = sort(args.width, args.height, args.length, args.mass)
    print(f'Label: {label}')


if __name__ == "__main__":
    main()
