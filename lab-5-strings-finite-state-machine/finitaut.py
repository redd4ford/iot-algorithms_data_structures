"""String matching with custom finite-state machine implementation."""
import doctest
from finite_state_machine import FiniteStateMachine


def read_from_file(file: str) -> tuple:
    """
    read from .in file.
    :param file: a file to read from
    :return: a string to be checked, and a pattern
    >>> string, pattern = read_from_file('examples/1.in')
    >>> print(string)
    abababacaba
    >>> print(pattern)
    ab
    """
    with open(file, 'r') as in_file:
        in_data = in_file.readlines()
        string = in_data[0].rstrip('\n')
        pattern = in_data[1].rstrip('\n')
    return string, pattern


def write_to_file(file: str, results: list) -> None:
    """
    write the results to .out file.
    :param file: a file to write to
    :param results: a list that contains start-end indexes pairs
    :return: none
    >>> write_to_file('examples/test.out', [[0, 1], [1, 2], [2, 3]])
    >>> with open('examples/test.out', 'r') as out_file:
    ...     out_data = out_file.readlines()
    ...     for line in out_data:
    ...         print(line) #doctest: +ELLIPSIS
    0 1...
    1 2...
    2 3
    >>> import os
    >>> os.remove('./examples/test.out')
    """
    with open(file, 'w') as out_file:
        first_line = True
        for indexes in results:
            line_to_write = ''
            if first_line:
                first_line = False
            else:
                line_to_write += '\n'

            line_to_write += str(indexes[0])
            if len(indexes) > 1:
                line_to_write += ' ' + str(indexes[1])
            out_file.write(line_to_write)


def main(IN_FILE='finitaut.in', OUT_FILE='finitaut.out') -> None:
    """
    using brute-force, check if each character of a potentially matching
    substring is equal to a current state of the finite automata. if yes,
    go to the next state. the substring is considered fully matching when
    the machine reaches its trailing state.
    :param IN_FILE: a file to read from
    :param OUT_FILE: a file to write to
    :return: none
    >>> main('examples/3.in', 'examples/3.out')
    >>> with open('examples/3.out', 'r') as out_file:
    ...     out_data = out_file.readlines()
    ...     for line in out_data:
    ...         print(line)
    11 15
    >>> main('examples/4.in', 'examples/4.out')
    >>> with open('examples/4.out', 'r') as out_file:
    ...     out_data = out_file.readlines()
    ...     for line in out_data:
    ...         print(line) #doctest: +ELLIPSIS
    0 3...
    3 6...
    6 9...
    9 12...
    12 15...
    15 18
    >>> main('examples/5.in', 'examples/5.out')
    >>> with open('examples/5.out', 'r') as out_file:
    ...     out_data = out_file.readlines()
    ...     for line in out_data:
    ...         print(line) #doctest: +ELLIPSIS
    0...
    1...
    2...
    3...
    4...
    5
    """
    string, pattern = read_from_file(file=IN_FILE)

    machine = FiniteStateMachine()
    machine.fill_states(pattern=pattern)

    results = []
    for seq_start_idx in range(0, len(string) - len(pattern) + 1):
        if machine.is_next_matching(symbol=string[seq_start_idx]):
            if len(pattern) == 1:
                results.append([seq_start_idx])

            else:
                machine.curr_state_idx = 1

                for seq_end_idx in range(seq_start_idx + 1, len(string)):
                    if machine.is_next_matching(symbol=string[seq_end_idx]):
                        machine.curr_state_idx += 1

                        if machine.is_curr_trailing():
                            results.append([seq_start_idx, seq_end_idx])
                        else:
                            continue
                    machine.curr_state_idx = 0
                    break

    write_to_file(file=OUT_FILE, results=results)


if __name__ == '__main__':
    doctest.testmod(verbose=True)
    main()
