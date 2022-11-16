
def convertArrToLinkedList(arr):
    prev = result = ListNode("#")
    for num in arr:
        prev.next = ListNode(num)
        prev = prev.next

    return result.next


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverse(head):
    prev = None
    current = head

    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    return prev