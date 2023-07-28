from typing import Optional


class ListNode:
    def __init__(self, val=0, nextNode=None):
        self.val = val
        self.nextNode = nextNode


class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_linked_list = Optional[ListNode]()
        while True:
            if (l1.nextNode == None or l2.nextNode == None):
                break
            if result_linked_list == None:
                result_linked_list = ListNode(l1.val + l2.val)

