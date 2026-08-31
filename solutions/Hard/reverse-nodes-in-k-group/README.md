# Reverse Nodes in k-Group

**Difficulty:** Hard  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/reverse-nodes-in-k-group/)

## Problem Description
Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return *the modified list*.

`k` is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg)

```
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg)

```
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
```

**Constraints:**

* The number of nodes in the list is `n`.
* `1 <= k <= n <= 5000`
* `0 <= Node.val <= 1000`

**Follow-up:** Can you solve the problem in `O(1)` extra memory space?

## Solution

- **Language:** Python3
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

### Approach
The algorithm uses a dummy node to simplify edge cases at the head of the list. We maintain a pointer `groupPrev` which points to the node immediately preceding the current group of size `k`. In each iteration, we find the `k`-th node from `groupPrev`. If fewer than `k` nodes remain, we terminate. Otherwise, we reverse the `k` nodes in-place. By initializing the `prev` pointer of our reversal loop to the node immediately following the group (`groupNext`), the reversed group automatically links to the rest of the list. Finally, we connect `groupPrev` to the new head of the reversed group and update `groupPrev` to the tail of the reversed group for the next iteration.

### Code
```py
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
```
