# Trapping Rain Water

**Difficulty:** Hard  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/trapping-rain-water/)

## Problem Description
Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

**Example 1:**

![](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)

```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
```

**Example 2:**

```
Input: height = [4,2,0,3,2,5]
Output: 9
```

**Constraints:**

* `n == height.length`
* `1 <= n <= 2 * 104`
* `0 <= height[i] <= 105`

## Solution

- **Language:** Python3
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

### Approach
We use the two-pointer approach to solve this problem in O(1) auxiliary space. We maintain two pointers, `left` at the beginning and `right` at the end of the array, along with `left_max` and `right_max` to keep track of the maximum height seen so far from both ends. At each step, we process the bar with the smaller height. If the current height is less than the max height seen from that side, it means water can be trapped above the current bar equal to `max_height - height[current]`. Otherwise, we update the maximum height for that side.

### Code
```py
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
                
        return water
```
