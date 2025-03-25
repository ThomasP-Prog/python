def print_3by3(matrix : list[list]) -> None:
    """Print 3X3 matrix"""
    for row in matrix:
        print(" | ".join(map(str, row)))

def transpose(matrix : list[list]) -> None:
    """Convert rows into columns"""
    """transpose_list = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(matrix)):
        for y in range(len(matrix[i])):
            transpose_list[i][y] = matrix[y][i]
    matrix[:] = transpose_list"""

    matrix[:] = [list(row) for row in zip(*matrix)]
    """The zip() function is used to group elements from multiple iterables (like lists).
       The *matrix syntax unpacks the rows of the matrix, meaning zip() will receive each row as a separate argument.
       Since zip() returns tuples, we need to convert them to lists.
       That's what list(row) does inside the list comprehension."""

def flatten(matrix : list[list]) -> None:
    """Flatten 3X3 matrix"""
    """flat_matrix = [0,0,0,0,0,0,0,0,0]
    for f in range(len(flat_matrix)):
        for i in range(len(matrix)):
            for y in range(len(matrix[i])):
                if f in range(len(flat_matrix)) and flat_matrix[f] == 0:
                    flat_matrix[f] = matrix[y][i]
                    print(flat_matrix)
                    f = f+1
    matrix[:] = flat_matrix"""

    matrix[:] = [item for row in matrix for item in row]
    """Each row is a list inside matrix, and we iterate through its elements (item) one by one.
    The outer loop (for row in matrix) iterates over each row (sublist).
    The inner loop (for item in row) iterates over each item in the row."""

def main() -> None:
    """Main function"""
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(matrix)
    print_3by3(matrix)
    transpose(matrix)
    print_3by3(matrix)
    flatten(matrix)
    print(matrix)

if __name__ == "__main__":
    main()