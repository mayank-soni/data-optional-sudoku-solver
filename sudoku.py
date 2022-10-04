# pylint: disable=missing-docstring
from collections import Counter

def sudoku_solver(grid):
    """Sudoku solver"""

    # Check grid validity:
    if (not isinstance(grid, list)
        or any(not isinstance(row, list) for row in grid)
        or len(grid) != 9
        or any(len(row) != 9 for row in grid)
    ):
        return "invalid grid"

    # try a random digit.
    # If it works, continue to next unknown.
    # if all digits fail,
    # go back one step

    # How to try a random digit
    # access each value in turn.
    # if value is 0, then change it

    # Loop over rows and columns of grid

    #Flatten table first
    flat_grid = [['Or', value] if value != 0 else ['Cr', 0] for row in grid for value in row]

    #Loop over flat table
    i = 0
    worked = True
    while i < len(flat_grid):
        #If value is empty (0)
        if flat_grid[i][0] == 'Cr':
            #Try values from 1-9 in turn
            for new_value in range(flat_grid[i][1] + 1, 10):
                flat_grid[i][1] = new_value
                flat_grid_no_tag = [ls[1] for ls in flat_grid]
                if partial_sudoku_validator([flat_grid_no_tag[j*9: j*9+9] for j in range(9)]):
                    worked = True
                    break
                # If all values tested already and still no success:
                if new_value == 9:
                    worked = False
            if worked:
                i += 1
            else:
                flat_grid[i][1] = 0
                i -= 1
        else:
            if worked:
                i += 1
            else:
                if i >= 1:
                    i -= 1
                else:
                    return "No Solution"
    return [flat_grid_no_tag[k*9: k*9+9] for k in range(9)]


def partial_sudoku_validator(grid):
    """
    Checks if a partial sudoku solution is valid (so far)
    Does so by seeing if count of any digit exceeds 1
    """

    # Check rows
    for row in grid:
        count = Counter(row)
        count[0] = 0
        if max(count.values()) > 1:
            return False

    # Check columns
    # zip(*grid) - gives an iterable over columns instead of rows
    for column in zip(*grid):
        count = Counter(column)
        count[0] = 0
        if max(count.values()) > 1:
            return False

    # Check squares
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            square = [value for row in grid[i:i+3] for value in row[j:j+3]]
            count = Counter(square)
            count[0] = 0
            if max(count.values()) > 1:
                return False

    return True

if __name__ == '__main__':
    print(sudoku_solver([[7,0,0,  0,0,9,  0,0,0],
    [0,0,0,  6,0,0,  0,4,0],
    [0,0,2,  0,0,0,  0,0,0],

    [0,0,0,  0,0,0,  4,0,0],
    [0,5,0,  0,4,6,  0,0,0],
    [0,0,0,  0,0,0,  0,0,0],

    [0,0,6,  0,0,0,  0,0,5],
    [2,0,0,  5,0,0,  0,0,0],
    [0,0,0,  0,0,0,  0,3,0]]))
