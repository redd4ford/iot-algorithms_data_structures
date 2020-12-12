import doctest


def knuth_morris_pratt(string: str, pattern: str) -> list:
    """
    implementation of Knuth-Morris-Pratt algorithm. if we detect a
    mismatch, we already know some elements of the next sequence and
    because of that can skip matching the characters that will match
    anyway. we get information about those elements from pre-processing
    the pattern. lps[] contains the count of characters to be skipped.
    :param string: a string to be checked
    :param pattern:
    :return result: a list that contains start-end indices of matching
    substrings pairs
    """
    if string is None or pattern is None or len(string) < len(pattern):
        return [0]

    results = []

    # pre-process the pattern is the key to the algorithm's efficiency.
    # track the length of the longest prefix suffix value for
    # the previous index. if pattern[prev_longest_pref_suf] and
    # pattern[curr_string_pos] match, increment prev_longest_pref_suf and
    # assign the incremented value to lps[curr_string_pos]. if the do not
    # match and prev_longest_pref_suf != 0, we update it to
    # lps[prev_longest_pref_suf - 1].

    # LPS stands for Longest Proper Prefix and Suffix
    lps = [0] * len(pattern)
    prev_longest_pref_suf = 0
    curr_pattern_pos = 1
    while curr_pattern_pos < len(pattern):
        if pattern[curr_pattern_pos] == pattern[prev_longest_pref_suf]:
            prev_longest_pref_suf += 1
            lps[curr_pattern_pos] = prev_longest_pref_suf
            curr_pattern_pos += 1
        else:
            if prev_longest_pref_suf != 0:
                prev_longest_pref_suf = lps[prev_longest_pref_suf - 1]
            else:
                lps[curr_pattern_pos] = 0
                curr_pattern_pos += 1

    curr_string_pos = 0
    curr_matching_pos = 0

    # if the next characters of the string and the pattern do not match,
    # we do NOT move the pattern to the first character and do NOT compare
    # it with the string from the very beginning (as we would do in
    # the naive algorithm). instead, we shift the pattern a few characters
    # and do one comparison of string[i] and pattern[j]. if they do not
    # match, shift the pattern again until the symbols match or we reach
    # the beginning of the pattern. thus, we do not move backwards along
    # the search line, only forward.

    while curr_string_pos < len(string):
        if pattern[curr_matching_pos] == string[curr_string_pos]:
            curr_string_pos += 1
            curr_matching_pos += 1

        if curr_matching_pos == len(pattern):
            if len(pattern) == 1:
                results.append([curr_string_pos - 1])
            else:
                results.append([curr_string_pos - curr_matching_pos,
                                curr_string_pos - 1])
            curr_matching_pos = lps[curr_matching_pos - 1]

        elif curr_string_pos < len(string) and \
                pattern[curr_matching_pos] != string[curr_string_pos]:
            if curr_matching_pos != 0:
                curr_matching_pos = lps[curr_matching_pos - 1]
            else:
                curr_string_pos += 1

    return results


def read_from_file(file: str) -> tuple:
    """
    read from .in file.
    :param file: a file to read from
    :return: a string to be checked, and a pattern
    >>> string, pattern = read_from_file('examples/1.in')
    >>> print(string)
    cabababcababaca
    >>> print(pattern)
    ababaca
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
    :param results: a list that contains start-end indexes pairs for each
    matching substring
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


def main(IN_FILE='SOOQA.in', OUT_FILE='kmpsubstr.out') -> None:
    """
    main function.
    :param IN_FILE: a file to read string and pattern values from
    :param OUT_FILE: a file to write the results to
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
    results = knuth_morris_pratt(string=string,
                                 pattern=pattern)
    write_to_file(file=OUT_FILE,
                  results=results)


if __name__ == '__main__':
    doctest.testmod(verbose=True)
    main('examples/1.in', 'examples/1.out')
