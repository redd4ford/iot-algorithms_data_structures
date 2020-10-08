from timeit import default_timer as timer
from datetime import timedelta
import csv_reader
import info_printer
import copy
from sort import *


def main():
    list_of_helicopters = csv_reader.csv_to_helicopters('helicopters.csv')

    print('========== INSERTION SORT - ASCENDING - BY MAX_SPEED ==========')

    start_time = timer()
    sorted_helicopters = insertion_sort_by_max_speed(copy.deepcopy(list_of_helicopters))
    elapsed_time = timedelta(seconds=timer() - start_time)

    info_printer.print_algorithm_info(elapsed_time, 'INSERTION')
    print('===============================================================')
    info_printer.print_list(sorted_helicopters)

    print('\n')
    print('========= MERGE SORT - DESCENDING - BY MAX_PASSENGERS =========')

    start_time = timer()
    sorted_helicopters = merge_sort_by_passengers(copy.deepcopy(list_of_helicopters))
    elapsed_time = timedelta(seconds=timer() - start_time)

    info_printer.print_algorithm_info(elapsed_time, 'MERGE')
    print('===============================================================')
    info_printer.print_list(sorted_helicopters)


if __name__ == '__main__':
    main()
