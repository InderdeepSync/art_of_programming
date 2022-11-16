'''
https://leetcode.com/problems/reverse-linked-list-ii/

Reverse Linked List II
Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.

'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_sublist(linked_list, left, right): 
    pass


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print(reverse_sublist(head, 1, 3))