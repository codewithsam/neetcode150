# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry =0
        dummy = ListNode()
        head = dummy
        while l1 or l2:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            total = l1val +l2val+carry
            carry = total//10
            num = total%10
            newNode = ListNode(num)
            dummy.next = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            dummy = dummy.next
        if carry != 0:
            node = ListNode(carry)
            dummy.next = node
        return head.next
    def convertToLinkedList(self, nums):
        dummy = ListNode()
        head = dummy
        for num in nums:
            newNode = ListNode(num)
            dummy.next = newNode
            dummy = dummy.next
        return head.next
sol = Solution()
head1 = sol.convertToLinkedList([9,9,9,9,9,9,9])
head2 = sol.convertToLinkedList([9,9,9,9])

h = sol.addTwoNumbers(head1, head2)
while h:
    print(h.val)
    h = h.next