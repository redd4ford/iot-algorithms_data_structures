import sort_counter


def insertion_sort_by_max_speed(helicopters):
    for current_pos in range(1, len(helicopters)):
        current_element = helicopters[current_pos]
        hole_pos = current_pos - 1

        while hole_pos >= 0:
            sort_counter.insert_comp_counter += 1
            if helicopters[hole_pos].max_speed > current_element.max_speed:
                sort_counter.insert_slip_counter += 1
                helicopters[hole_pos + 1] = helicopters[hole_pos]
                hole_pos -= 1
            else:
                break

        helicopters[hole_pos + 1] = current_element

    return helicopters


def merge_sort_by_passengers(helicopters):
    if len(helicopters) > 1:
        middle_pos = len(helicopters) // 2
        left = helicopters[:middle_pos]
        right = helicopters[middle_pos:]

        left = merge_sort_by_passengers(left)
        right = merge_sort_by_passengers(right)

        helicopters = []

        while len(left) > 0 and len(right) > 0:
            if left[0].max_passengers > right[0].max_passengers:
                helicopters.append(left[0])
                left.pop(0)
            else:
                helicopters.append(right[0])
                right.pop(0)

        for element in left:
            helicopters.append(element)
        for element in right:
            helicopters.append(element)

    return helicopters
