# Next Permutation

**Difficulty:** Medium  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/next-permutation/)

## Problem Description
A **permutation** of an array of integers is an arrangement of its members into a sequence or linear order.

* For example, for `arr = [1,2,3]`, the following are all the permutations of `arr`: `[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1]`.

The **next permutation** of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the **next permutation** of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

* For example, the next permutation of `arr = [1,2,3]` is `[1,3,2]`.
* Similarly, the next permutation of `arr = [2,3,1]` is `[3,1,2]`.
* While the next permutation of `arr = [3,2,1]` is `[1,2,3]` because `[3,2,1]` does not have a lexicographical larger rearrangement.

Given an array of integers `nums`, *find the next permutation of* `nums`.

The replacement must be **[in place](http://en.wikipedia.org/wiki/In-place_algorithm)** and use only constant extra memory.

**Example 1:**

```
Input: nums = [1,2,3]
Output: [1,3,2]
```

**Example 2:**

```
Input: nums = [3,2,1]
Output: [1,2,3]
```

**Example 3:**

```
Input: nums = [1,1,5]
Output: [1,5,1]
```

**Constraints:**

* `1 <= nums.length <= 100`
* `0 <= nums[i] <= 100`

## Solution

- **Language:** Python3
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

### Approach
To find the next lexicographically greater permutation:
1. Find the largest index `i` from right to left such that `nums[i] < nums[i + 1]`. If no such index exists, the entire array is sorted in descending order, so we reverse it to form the smallest permutation.
2. If `i` is found, search from right to left for the largest index `j` such that `nums[j] > nums[i]`.
3. Swap `nums[i]` and `nums[j]`.
4. Reverse the suffix starting from index `i + 1` to the end of the array to place it in ascending order, ensuring the next permutation is as small as possible.

### Code
```py
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
```
