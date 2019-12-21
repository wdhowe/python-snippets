#!/usr/bin/env python3
"""
Single linked list examples
"""


class ListNode:
    """
    Single linked list class
    """

    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


def print_list(start_node: ListNode):
    """
    Print all nodes in the list starting at the
    passed in node
    """
    ptr = start_node
    while True:
        print(f"Data is: {ptr.data}")
        print(f"Next is: {ptr.next}")
        if ptr.next is None:
            break
        else:
            ptr = ptr.next


def insert_after(after_node: ListNode, new_node: ListNode):
    """
    Insert a node (new_node) into the linked list
    after the 'after_node'
    """
    new_node.next = after_node.next
    after_node.next = new_node


def search_list(search_node: ListNode, search_key: int):
    """
    Traverse the list and search for the data passed in
    as the search_key
    """
    while search_node and search_node.data != search_key:
        search_node = search_node.next
    return search_node


def main():
    """
    Simple single list list demo
    """

    print(f"Single Linked List testing")

    # Create an initial 1 node linked list
    node01 = ListNode(10, None)

    # Insert some more nodes
    insert_after(node01, ListNode(20))
    insert_after(node01.next, ListNode(40))

    print("\nPrinting all nodes.")
    print_list(node01)

    search_num = 40
    print(f"\nSearching for {search_num}")
    result = search_list(node01, search_num)

    if result:
        print(f"Found. Data was: {result.data}")
    else:
        print(f"No result found.")


if __name__ == "__main__":
    main()
