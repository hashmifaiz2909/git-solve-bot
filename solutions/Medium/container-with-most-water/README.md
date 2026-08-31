# Container With Most Water

**Difficulty:** Medium  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/container-with-most-water/)

## Problem Description
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return *the maximum amount of water a container can store*.

**Notice** that you may not slant the container.

**Example 1:**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```

**Example 2:**

```
Input: height = [1,1]
Output: 1
```

**Constraints:**

* `n == height.length`
* `2 <= n <= 105`
* `0 <= height[i] <= 104`

## Solution

- **Language:** Python3
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

### Approach
The problem can be solved efficiently using a two-pointer approach. We initialize two pointers, one at the beginning (`left = 0`) and one at the end (`right = len(height) - 1`) of the array. At each step, we calculate the area of the container formed by the lines at these two pointers. The area is determined by the shorter of the two lines multiplied by the distance between them. To maximize the area, we always move the pointer pointing to the shorter line inward, because keeping the shorter line would never yield a larger area as the width decreases. We repeat this process until the two pointers meet, keeping track of the maximum area found.

### Code
```py
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            h_left = height[left]
            h_right = height[right]
            current_area = min(h_left, h_right) * (right - left)
            if current_area > max_area:
                max_area = current_area
            
            if h_left < h_right:
                left += 1
            else:
                right -= 1
                
        return max_area
```
