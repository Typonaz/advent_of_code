from math import *

def reading(file_name):
    file = open(file_name)
    array = file.read().splitlines()
    file.close()
    return array


def row_region(row_letter, row_range):
    if row_letter == 'F':
        row_range[1] -= ceil((row_range[1] - row_range[0]) / 2)
    else:
        row_range[0] += ceil((row_range[1] - row_range[0]) / 2)
    return row_range


def row_position(row_letters):
    row_range = [0, 127]
    for row_letter in row_letters:
        row_range = row_region(row_letter, row_range)
    return row_range[0]


def col_region(col_letter, col_range):
    if col_letter == 'L':
        col_range[1] -= ceil((col_range[1] - col_range[0]) / 2)
    else:
        col_range[0] += ceil((col_range[1] - col_range[0]) / 2)
    return col_range


def col_position(col_letters):
    col_range = [0, 7]
    for col_letter in col_letters:
        col_range = col_region(col_letter, col_range)
    return col_range[0]


def calc_seat_IDs(boarding_passes):
    seat_IDs = []
    for boarding_passe in boarding_passes:
        position = row_position(boarding_passe[:-3]) * 8 + col_position((boarding_passe[-3:]))
        seat_IDs.append(position)
    return seat_IDs


def upper_seat_ID(seat_IDs):
    current_seat_ID = 0
    for seat_ID in seat_IDs:
        if current_seat_ID < int(seat_ID):
            current_seat_ID = seat_ID
    return current_seat_ID


def lower_seat_ID(seat_IDs):
    current_seat_ID = upper_seat_ID(seat_IDs)
    for seat_ID in seat_IDs:
        if current_seat_ID > int(seat_ID):
            current_seat_ID = seat_ID
    return current_seat_ID


def missing_seat_ID(max_seat_ID, min_seat_ID, seat_IDs):
    for seat_ID in range (min_seat_ID, max_seat_ID):
        if not seat_ID in seat_IDs:
            return seat_ID


boarding_passes = reading("inputs.txt")
print("Puzzle 1 =", upper_seat_ID(calc_seat_IDs(boarding_passes)))

max_seat_ID = upper_seat_ID(calc_seat_IDs(boarding_passes))
min_seat_ID = lower_seat_ID(calc_seat_IDs(boarding_passes))

print("Puzzle 2 =", missing_seat_ID(max_seat_ID, min_seat_ID, calc_seat_IDs(boarding_passes)))





