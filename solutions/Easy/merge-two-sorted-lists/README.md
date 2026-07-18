# Merge Two Sorted Lists

**Difficulty:** Easy  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/merge-two-sorted-lists/)

## Problem Description
You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return *the head of the merged linked list*.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

**Example 2:**

```
Input: list1 = [], list2 = []
Output: []
```

**Example 3:**

```
Input: list1 = [], list2 = [0]
Output: [0]
```

**Constraints:**

* The number of nodes in both lists is in the range `[0, 50]`.
* `-100 <= Node.val <= 100`
* Both `list1` and `list2` are sorted in **non-decreasing** order.

## Solution

- **Language:** Python3
- **Time Complexity:** O(N + M)
- **Space Complexity:** O(1)

### Approach
The algorithm uses a dummy node to easily build the merged list. We maintain a pointer `curr` to track the end of the merged list. We compare the values of the current nodes of `list1` and `list2`, appending the smaller node to `curr.next` and advancing the pointer of that list. Once one of the lists is exhausted, we append the remainder of the other list to `curr.next` and return `dummy.next`.

### Code
```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        curr.next = list1 if list1 is not None else list2
        
        return dummy.next
```
