"""IJONES problem solution."""
import doctest
from collections import defaultdict


def get_paths_number(corridor: list, height: int, width: int) -> int:
    """
    for each element of each column starting from the end, check if it
    does not lead to a dead end, and add all the known paths for this
    letter so far. when a column ends, update the totals for each letter
    so that we know there are more possible paths going through the plates
    we have already visited.
    :param corridor: the list of lines that contain plates
    :param height: the height of the corridor
    :param width: the width of the corridor
    :return: sum of solutions found for each line
    >>> print(get_paths_number(['afgh', 'hhab', 'aaaa'], 3, 4))
    16
    """
    solutions_in_line = [0] * height
    endpoints = set()
    plates_visited_count = defaultdict(int)

    for i in (0, height - 1):
        endpoint_plate = corridor[i][width - 1]
        # lines that contain endpoint plates (the first and the last ones)
        # are guaranteed to have one path
        solutions_in_line[i] = 1
        endpoints.add(endpoint_plate)
        plates_visited_count[endpoint_plate] += 1

    for j in range(width - 2, -1, -1):
        current_column_paths_count = defaultdict(int)

        for i in range(height):
            plate = corridor[i][j]
            if plate not in endpoints and solutions_in_line[i] == 0:
                continue
            plate_solution_count = plates_visited_count[plate]

            if plate is not corridor[i][j + 1]:
                plate_solution_count += solutions_in_line[i]

            solutions_in_line[i] = plate_solution_count
            # the totals for each plate will be updated when the column
            # is finished
            current_column_paths_count[plate] += plate_solution_count

        # update visited_counters for all the plates of this column
        for plate_key in current_column_paths_count:
            endpoints.add(plate_key)
            plates_visited_count[plate_key] += current_column_paths_count[plate_key]

    return sum(solutions_in_line)


def main(IN_FILE='ijones.in', OUT_FILE='ijones.out') -> None:
    """
    get the width and the height of the corridor and its lines, then use
    the data for calculations and write the result to an output file.
    :param IN_FILE: the name of the input file
    :param OUT_FILE: the name of the output file
    :return: none
    >>> main('examples/1.in', 'examples/1.out')
    >>> print(open('examples/1.out', 'r').readline())
    5
    >>> main('examples/2.in', 'examples/2.out')
    >>> print(open('examples/2.out', 'r').readline())
    2
    >>> main('examples/3.in', 'examples/3.out')
    >>> print(open('examples/3.out', 'r').readline())
    201684
    """
    with open(IN_FILE, 'r') as in_file:
        in_data = in_file.readlines()
    width, height = map(int, in_data[0].split(' '))
    corridor = [in_data[line].rstrip('\n') for line in range(1, height + 1)]

    paths_number = get_paths_number(corridor, height, width)

    open(OUT_FILE, 'w').write(str(paths_number))


if __name__ == '__main__':
    doctest.testmod(verbose=True)
    main()
