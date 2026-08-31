# Remove Duplicates from Sorted List II

**Difficulty:** Medium  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)

## Problem Description
Given the `head` of a sorted linked list, *delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list*. Return *the linked list **sorted** as well*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/04/linkedlist1.jpg)

```
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/01/04/linkedlist2.jpg)

```
Input: head = [1,1,1,2,3]
Output: [2,3]
```

**Constraints:**

* The number of nodes in the list is in the range `[0, 300]`.
* `-100 <= Node.val <= 100`
* The list is guaranteed to be **sorted** in ascending order.

## Solution

- **Language:** Python3
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

### Approach
We use a dummy head node pointing to the head of the linked list to simplify edge cases where the head node itself needs to be removed. We traverse the list using two pointers: `prev` (which tracks the last confirmed distinct node) and `head` (which scans the list). At each node, we check if it has duplicates by comparing its value to `head.next.val`. If duplicates exist, we advance `head` until the end of the duplicate sequence and link `prev.next` to the node after the duplicates. If no duplicate exists, we simply move `prev` forward. Finally, we advance `head` to continue scanning until the end of the list.

### Code
```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
            
        return dummy.next
```
