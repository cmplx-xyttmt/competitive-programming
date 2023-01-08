def floor_div(x: int, y: int) -> int:
    """
    Gets the floor of x/y (and handles the cases where x or y are negative)
    :return: floor(x/y)
    """
    if x >= 0:
        return x // y
    else:
        return (x - y + 1) // y
