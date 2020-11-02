class Node:
    def __init__(self, index, value, next_node):
        self.index = index
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, value, next_node):
        new_element = Node(self.length, value, next_node)
        if new_element.index == 0:
            self.head = new_element
        else:
            previous = self.get_by_index(self.length - 1)
            previous.next = new_element
        self.length += 1

    def get_by_index(self, index):
        current = self.head
        found = False
        while current and not found:
            if current.index == index:
                found = True
            else:
                current = current.next
        if current is None:
            raise Exception('No element with such index')
        return current

    def merge(self, left, right):
        if left is None:
            return right
        elif right is None:
            return left

        if left.value <= right.value:
            result = left
            result.next = self.merge(left.next, right)
        else:
            result = right
            result.next = self.merge(left, right.next)
        return result

    def sort(self, head: Node):
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

        sorted_list = self.merge(left, right)

        return sorted_list

    def order(self):
        current_node = self.head
        index = 0
        while current_node:
            current_node.index = index
            index += 1
            current_node = current_node.next


def main():
    cards = LinkedList()
    jokers_count = 0

    for element in open('lngpok.in', 'r').readline().split():
        if cards.length == 10000:
            raise Exception('Player cannot have more than 10 000 cards.')
        if int(element) == 0:
            jokers_count += 1
        else:
            cards.add(int(element), None)

    cards.head = cards.sort(cards.head)
    cards.order()

    jokers_buffer = jokers_count
    sequence_length = 1
    max_sequence_length = 1
    current_pos = 1

    if cards.length > 1:
        while current_pos < cards.length:
            difference = cards.get_by_index(current_pos).value -\
                         cards.get_by_index(current_pos - 1).value
            if difference < 2:
                if difference == 1:
                    sequence_length += 1
                current_pos += 1
                continue
            current_pos += 1

            jokers_left = jokers_buffer - difference + 1

            if jokers_left >= 0:
                sequence_length += difference
                jokers_buffer = jokers_left
            else:
                sequence_length += jokers_buffer
                jokers_buffer = jokers_count
                if sequence_length > max_sequence_length:
                    max_sequence_length = sequence_length
                sequence_length = 1

        if jokers_buffer:
            sequence_length += jokers_buffer
        if sequence_length > max_sequence_length:
            max_sequence_length = sequence_length

    elif cards.length <= 1:
        max_sequence_length = jokers_count + cards.length

    open('lngpok.out', 'w').write(str(max_sequence_length))


if __name__ == '__main__':
    main()
