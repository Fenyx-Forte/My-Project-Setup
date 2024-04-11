def calculate_area_square(length: int | float) -> int | float:
    """Function to calculate the area of a square

    Args:
        length (int | float): length of the square

    Raises:
        TypeError: if length is not a positive non-zero number

    Returns:
        int | float: area of the square
    """
    if not isinstance(length, (int, float)) or length <= 0:
        raise TypeError("Length must be a positive non-zero number")

    return length * length
