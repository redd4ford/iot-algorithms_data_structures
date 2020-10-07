from helicopter import Helicopter
import csv


def csv_to_helicopters(file_name: str):
    helicopters = []
    csv_file = open(file_name, 'r')
    for row in csv.reader(csv_file):
        helicopters.append(Helicopter(row[0],
                                      int(row[1]),
                                      int(row[2])))
    return helicopters
