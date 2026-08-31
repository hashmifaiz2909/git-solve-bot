# Merge k Sorted Lists

**Difficulty:** Hard  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/merge-k-sorted-lists/)

## Problem Description
You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

*Merge all the linked-lists into one sorted linked-list and return it.*

**Example 1:**

```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
```

**Example 2:**

```
Input: lists = []
Output: []
```

**Example 3:**

```
Input: lists = [[]]
Output: []
```

**Constraints:**

* `k == lists.length`
* `0 <= k <= 104`
* `0 <= lists[i].length <= 500`
* `-104 <= lists[i][j] <= 104`
* `lists[i]` is sorted in **ascending order**.
* The sum of `lists[i].length` will not exceed `104`.

## Solution

- **Language:** Python3
- **Time Complexity:** O(N log k), where N is the total number of nodes across all lists and k is the number of linked lists. Each node insertion and extraction from the min-heap takes O(log k) time.
- **Space Complexity:** O(k), since the min-heap stores at most one node from each of the k lists at any given time.

### Approach
We use a min-heap (priority queue) to efficiently find the smallest node among the heads of the k lists. First, we push the head of each non-empty list into the heap, storing a tuple `(node.val, index, node)` to avoid direct object comparison when values are identical. We iteratively extract the smallest node from the min-heap, attach it to our result list, and push its next node into the heap if it exists. This continues until the heap is empty.

### Code
```py
import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        curr = dummy
        
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next
```
