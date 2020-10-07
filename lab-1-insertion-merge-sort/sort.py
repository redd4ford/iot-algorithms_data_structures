import sort_counter


def insertion_sort_by_max_speed(helicopters):
    for current_pos in range(1, len(helicopters)):
        current_element = helicopters[current_pos]
        hole_pos = current_pos - 1

        while hole_pos >= 0:
            sort_counter.insert_comp_counter += 1
            if helicopters[hole_pos].max_speed > current_element.max_speed:
                helicopters[hole_pos + 1] = helicopters[hole_pos]
                sort_counter.insert_slip_counter += 1
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

        left_pos = right_pos = original_pos = 0

        while left_pos < len(left) and right_pos < len(right):
            sort_counter.merge_comp_counter += 1
            if left[left_pos].max_passengers > right[right_pos].max_passengers:
                helicopters[original_pos] = left[left_pos]
                left_pos += 1
            else:
                helicopters[original_pos] = right[right_pos]
                right_pos += 1
            original_pos += 1
            sort_counter.merge_swap_counter += 1

        while left_pos < len(left):
            helicopters[original_pos] = left[left_pos]
            sort_counter.merge_comp_counter += 1
            left_pos += 1
            original_pos += 1

        while right_pos < len(right):
            helicopters[original_pos] = right[right_pos]
            sort_counter.merge_comp_counter += 1
            right_pos += 1
            original_pos += 1

    return helicopters
