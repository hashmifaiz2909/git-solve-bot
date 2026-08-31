class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            
            # Reverse the group of k nodes
            prev = groupNext
            curr = groupPrev.next
            tmp_head = curr
            for _ in range(k):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # Connect the previous group to the reversed group
            groupPrev.next = prev
            # Move groupPrev to the end of the reversed group
            groupPrev = tmp_head
            
        return dummy.next
        
    def getKth(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
