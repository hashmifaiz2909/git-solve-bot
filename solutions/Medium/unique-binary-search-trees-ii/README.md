# Unique Binary Search Trees II

**Difficulty:** Medium  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/unique-binary-search-trees-ii/)

## Problem Description
Given an integer `n`, return *all the structurally unique **BST'**s (binary search trees), which has exactly* `n` *nodes of unique values from* `1` *to* `n`. Return the answer in **any order**.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/18/uniquebstn3.jpg)

```
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
```

**Example 2:**

```
Input: n = 1
Output: [[1]]
```

**Constraints:**

* `1 <= n <= 8`

## Solution

- **Language:** Python3
- **Time Complexity:** O(4^n / n^(1.5))
- **Space Complexity:** O(4^n / n^(1.5))

### Approach
The problem can be solved using a recursive divide-and-conquer approach with memoization. For a range of numbers from `start` to `end`, we can pick any number `i` in this range to be the root of the BST. The left subtree will then be constructed from the range `[start, i - 1]` and the right subtree from `[i + 1, end]`. We recursively generate all possible left and right subtrees, and then combine them with the root `i`. To avoid redundant calculations, we use a memoization dictionary `memo` keyed by `(start, end)`.

### Code
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        
        memo = {}
        
        def generate(start, end):
            if start > end:
                return [None]
            if (start, end) in memo:
                return memo[(start, end)]
            
            all_trees = []
            for i in range(start, end + 1):
                left_trees = generate(start, i - 1)
                right_trees = generate(i + 1, end)
                
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)
            memo[(start, end)] = all_trees
            return all_trees
        
        return generate(1, n)
```
