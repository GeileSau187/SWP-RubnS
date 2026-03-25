import random

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListIterator:
    def __init__(self, start_node):
        self.current = start_node

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        value = self.current.value
        self.current = self.current.next
        return value


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.length += 1
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node
        self.length += 1

    def size(self):
        return self.length

    def print_all(self):
        current = self.head

        if current is None:
            print("List ist leer")
            return

        while current is not None:
            print(current.value)
            current = current.next

    def __iter__(self):
        return LinkedListIterator(self.head)


def main():
    linked_list = LinkedList()

    amount_of_numbers = 10
    min_value = 1
    max_value = 100

    for _ in range(amount_of_numbers):
        random_number = random.randint(min_value, max_value)
        linked_list.append(random_number)

    print("Länge der Liste")
    print(linked_list.size())

    print("\n Alle Elemente mit print_all():")
    linked_list.print_all()

    print("\n Alle Elemente mit Iterator:")
    for value in linked_list:
        print(value)


if __name__ == "__main__":
    main()