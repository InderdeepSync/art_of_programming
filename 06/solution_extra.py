
class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def reverse(head, prev=None):
    current = head

    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    return prev

def reverse_sublist(linked_list, left, right): # Verified on Leetcode
    linked_list = ListNode("X", next=linked_list)

    current = linked_list

    index = 0
    prev_left = left_node = right_node = None
    while current:
        if index == left - 1:
            prev_left = current
        if index == left:
            left_node = current
        if index == right:
            right_node = current

        index += 1
        current = current.next

    next_right = right_node.next
    right_node.next = None
    prev_left.next = reverse(left_node, next_right)

    return linked_list.next