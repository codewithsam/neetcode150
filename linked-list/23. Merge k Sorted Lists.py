# Definition for singly-linked list.
from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        pq = []
        for list in lists:
            heapq.heappush(pq, (list.val, id(list), list))
        
        while pq:
            _,_,node = heapq.heappop(pq)
            dummy.next = node
            dummy = dummy.next
            if node.next:
                heapq.heappush(pq, (node.next.val, id(node.next), node.next))
        return head.next
    def insertList(self,nums):
        dummy = ListNode()
        head = dummy
        for num in nums:
            newNode = ListNode(num)
            dummy.next = newNode
            dummy = dummy.next
        return head.next
    
sol = Solution()
l1 = sol.insertList([1,4,5])
l2 = sol.insertList([1,3,4])
l3 = sol.insertList([2,6])
head = sol.mergeKLists([l1,l2,l3])

while head:
    print(head.val)
    head = head.next