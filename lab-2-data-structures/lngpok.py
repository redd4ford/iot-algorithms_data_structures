"""LNGPOK problem solution."""
import doctest
import copy


class Node:
    """
    custom linked list node implementation.
    """

    def __init__(self, index, value, next_node):
        self.index = index
        self.value = value
        self.next = next_node


class LinkedList:
    """
    custom linked list implementation.
    """

    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, value, next_node):
        """
        add node to the linked list.
        :param value: the data to be stored
        :param next_node: the pointer to the next node in the linked list
        :return: none
        >>> test_list = LinkedList()
        >>> test_list.add(5, None)
        >>> print(str(test_list.get_by_index(0).value))
        5
        >>> print(test_list.head == test_list.get_by_index(0))
        True
        """
        new_element = Node(self.length, value, next_node)
        if new_element.index == 0:
            self.head = new_element
        else:
            previous = self.get_by_index(self.length - 1)
            previous.next = new_element
        self.length += 1

    def get_by_index(self, index):
        """
        get node by its index in the linked list.
        :param index: the index of element to be searched for
        :return: node with index equal to :param index:
        >>> test_list = LinkedList()
        >>> test_list.add(5, None)
        >>> print(str(test_list.get_by_index(0).value))
        5
        """
        if index >= self.length:
            raise Exception('Index out of range')
        current = self.head
        while current:
            if current.index == index:
                return current
            else:
                current = current.next
        if current is None:
            raise Exception('No element with such index')

    def __merge(self, left, right):
        """
        merge two sorted linked lists.
        :param left: first linked list
        :param right: second linked list
        :return: merged linked list
        """
        if left is None:
            return right
        elif right is None:
            return left

        if left.value <= right.value:
            result = left
            result.next = self.__merge(left.next, right)
        else:
            result = right
            result.next = self.__merge(left, right.next)
        return result

    def sort(self, head: Node):
        """
        sort the linked list using merge sorting algorithm.
        :param head: the head node of the linked list
        :return: sorted linked list
        >>> test_list = LinkedList()
        >>> test_list.add(5, None)
        >>> test_list.add(1, None)
        >>> test_list.add(13, None)
        >>> test_list.add(7, None)
        >>> test_list.head = test_list.sort(test_list.head)
        >>> test_list.print() #doctest: +ELLIPSIS
        1 5 7 13...
        """
        if head is None or head.next is None:
            return head

        middle = head
        next_peek = head
        while (next_peek.next is not None and
               next_peek.next.next is not None):
            middle = middle.next
            next_peek = next_peek.next.next

        next_to_middle = middle.next
        middle.next = None

        left = self.sort(head)
        right = self.sort(next_to_middle)

        sorted_list = self.__merge(left, right)

        return sorted_list

    def order(self):
        """
        set indexes for each node of the linked list.
        :return: none
        >>> test_list = LinkedList()
        >>> test_list.add(5, None)
        >>> test_list.add(1, None)
        >>> test_list.add(13, None)
        >>> test_list.add(7, None)
        >>> test_list.head = test_list.sort(test_list.head)
        >>> print(str(test_list.get_by_index(0).value))
        5
        >>> test_list.order()
        >>> print(str(test_list.get_by_index(0).value))
        1
        """
        current_node = self.head
        index = 0
        while current_node:
            current_node.index = index
            index += 1
            current_node = current_node.next

    def print(self):
        """
        utility function. print the linked list.
        :return: none
        >>> test_list = LinkedList()
        >>> test_list.add(6, None)
        >>> test_list.add(2, None)
        >>> test_list.add(12, None)
        >>> test_list.add(8, None)
        >>> test_list.print() #doctest: +ELLIPSIS
        6 2 12 8...
        """
        if self.head is None:
            raise Exception('The linked list is empty')
        curr_node = self.head
        while curr_node:
            print(curr_node.value, end=' ')
            curr_node = curr_node.next


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

    sequence_length = 1
    max_sequence_length = 1

    if cards.length <= 1:
        max_sequence_length = jokers_count + cards.length
    else:
        cards.head = cards.sort(cards.head)
        cards.order()

        jokers_buffer = jokers_count

        current_element = cards.head
        while current_element.next is not None:
            difference = copy.deepcopy(current_element.next.value) - copy.deepcopy(current_element.value)
            if difference < 2:
                if difference == 1:
                    sequence_length += 1
                current_element = copy.deepcopy(current_element.next)
                continue

            jokers_left = jokers_buffer - (difference - 1)

            if jokers_left >= 0:
                sequence_length += difference
                jokers_buffer = jokers_left
            else:
                sequence_length += jokers_buffer
                jokers_buffer = jokers_count
                if sequence_length > max_sequence_length:
                    max_sequence_length = copy.deepcopy(sequence_length)
                sequence_length = 1
            current_element = copy.deepcopy(current_element.next)

        if jokers_buffer:
            sequence_length += jokers_buffer
        if sequence_length > max_sequence_length:
            max_sequence_length = copy.deepcopy(sequence_length)

    open('lngpok.out', 'w').write(str(max_sequence_length))


if __name__ == '__main__':
    # doctest.testmod(verbose=True)
    main()
