"""Custom Linked List."""


class Node:
    """
    custom linked list node implementation.
    each node contains its data and a pointer to the next node.
    """

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    """
    custom linked list implementation.
    linked list is a linear data structure consists of nodes where each node
    contains a data field and a reference (link) to the next node in the list.
    """

    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, value, next_node):
        """
        add node to the end of the linked list. access the last element of this
        linked list and link a new node to it.
        :param value: the data to be stored
        :param next_node: the pointer to the next node in the linked list
        :return: none
        >>> test_list = LinkedList()
        >>> test_list.add(5, None)
        >>> print(str(test_list.head.value))
        5
        >>> test_list.add(7, None)
        >>> print(test_list.head.next is not None)
        True
        >>> print(test_list.head.next.value == 7)
        True
        """
        new_element = Node(value, next_node)
        if self.length == 0:
            self.head = new_element
        elif self.length == 1:
            self.head.next = new_element
        else:
            current = self.head.next
            while current.next:
                current = current.next
            current.next = new_element
        self.length += 1

    def __merge(self, left, right):
        """
        join two sorted linked lists. if any of the lists is empty, we return
        the other one. then compare data of these lists, set the smaller one
        to result, and merge again after incrementing the iterator
        of that list.
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

    @staticmethod
    def _get_middle(head):
        """
        utility method to get the middle of the linked list. use next_peek
        to look through the next two nodes. thus, if LinkedList.length
        is even, the middle will divide the list in such a way that one part
        of it is larger than the other by one.
        :param head: the head node of the linked list
        :return: middle node
        """
        middle = head
        next_peek = head
        while (next_peek.next is not None and
               next_peek.next.next is not None):
            middle = middle.next
            next_peek = next_peek.next.next
        return middle

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

        middle = LinkedList._get_middle(head)

        next_to_middle = middle.next
        middle.next = None

        left = self.sort(head)
        right = self.sort(next_to_middle)

        sorted_list = self.__merge(left, right)

        return sorted_list

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
