"""LNGPOK problem solution."""
import doctest
from linked_list import LinkedList


def main():
    """
    read the linked list from file, sort the sequence of cards, then incrementally
    move forward while building consecutive sequences and using joker cards
    to fill the gaps between elements if possible.
    :return: none
    >>> for element in open('lngpok.out', 'r').readline().split(): print(str(element))
    7
    """
    cards = LinkedList()
    jokers_count = 0

    for element in open('lngpok.in', 'r').readline().split():
        if cards.length == 10000:
            raise Exception('Player cannot have more than 10 000 cards.')
        if int(element) == 0:
            jokers_count += 1
        else:
            cards.add(int(element), None)

    max_sequence_length = 1

    if cards.length <= 1:
        max_sequence_length = jokers_count + cards.length
    else:
        cards.head = cards.sort(cards.head)

        current_element = cards.head
        while current_element is not None:
            sequence_length = 1
            jokers_buffer = jokers_count

            next_element = current_element.next
            previous_element = current_element
            while next_element is not None:
                gap_size = (next_element.value - previous_element.value) - 1

                if gap_size >= 0:
                    if gap_size < 2:
                        sequence_length += 1
                    if gap_size > 0:
                        if jokers_buffer >= gap_size:
                            sequence_length += gap_size
                            jokers_buffer -= gap_size
                        else:
                            sequence_length += jokers_buffer
                            jokers_buffer = 0
                            break

                previous_element = next_element
                next_element = next_element.next

            sequence_length += jokers_buffer
            if sequence_length > max_sequence_length:
                max_sequence_length = sequence_length
            current_element = current_element.next

    open('lngpok.out', 'w').write(str(max_sequence_length))


if __name__ == '__main__':
    # doctest.testmod(verbose=True)
    main()
