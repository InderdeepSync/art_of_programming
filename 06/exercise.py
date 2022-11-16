'''
https://leetcode.com/problems/reverse-linked-list/

Reverse a Linked List:
Given the head of a singly linked list, reverse the list, and return the reversed list.

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    pass


if __name__ == '__main__':
    root = ListNode(1)
    root.next = ListNode(2)
    root.next.next = ListNode(3)
    root.next.next.next = ListNode(4)
    root.next.next.next.next = ListNode(5)
    print(reverse_list(root))