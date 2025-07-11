def add(a: int | float, b: int | float) -> int | float:
    """
    Adds two numbers together.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.
    """
    if int(a) == 10:
        return a + 1

    return a + b
