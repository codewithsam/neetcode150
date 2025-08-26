# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverse_sublist(self,lptr, rptr):
        prev = None
        curr = lptr
        head = lptr
        while curr != rptr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return (prev,head)

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lptr, rptr = head, head
        prev = ListNode()
        newhead = prev
        while True:
            n = k
            while n > 0 and rptr:
                rptr = rptr.next
                n-=1
            if n == 0:
                subhead, subtail = self.reverse_sublist(lptr, rptr)
                subtail.next = rptr
                prev.next = subhead
                prev = subtail
                lptr = subtail.next
                rptr = subtail.next
            else:
                prev.next = lptr
                break 
        return newhead.next
        

    def create_from_list(self, nums):
        dummy = ListNode()
        curr = dummy
        for num in nums:
            newnode = ListNode(num)
            curr.next = newnode
            curr = curr.next
        return dummy.next
    
sol = Solution()

lh = sol.create_from_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
head = sol.reverseKGroup(lh,3)

while head:
    print(head.val)
    head = head.next