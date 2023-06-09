def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list): A matrix represented as a list of lists containing integers or floats.
        div (int or float): The divisor.

    Returns:
        list: A new matrix with the elements divided by the divisor, rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a matrix of integers/floats, or if the rows have different sizes,
                   or if the divisor is not a number.
        ZeroDivisionError: If the divisor is zero.
    """
    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) for row in matrix) or not all(
        isinstance(num, (int, float)) for row in matrix for num in row
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform matrix division and round to 2 decimal places
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix

