# Remove Duplicates from Sorted Array II

**Difficulty:** Medium  
**LeetCode Link:** [Open Problem](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

## Problem Description
Given an integer array `nums` sorted in **non-decreasing order**, remove some duplicates [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm) such that each unique element appears **at most twice**. The **relative order** of the elements should be kept the **same**.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the **first part** of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k` *after placing the final result in the first* `k` *slots of* `nums`.

Do **not** allocate extra space for another array. You must do this by **modifying the input array [in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** with O(1) extra memory.

**Custom Judge:**

The judge will test your solution with the following code:

```
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

If all assertions pass, then your solution will be **accepted**.

**Example 1:**

```
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

**Example 2:**

```
Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

**Constraints:**

* `1 <= nums.length <= 3 * 104`
* `-104 <= nums[i] <= 104`
* `nums` is sorted in **non-decreasing** order.

## Solution

- **Language:** Python3
- **Time Complexity:** O(N)
- **Space Complexity:** O(1)

### Approach
The algorithm uses a two-pointer approach. Since each unique element can appear at most twice, the first two elements of the array are always kept. We initialize a pointer `i` at index 2, which represents the position where the next valid element should be placed. We then iterate through the array with a pointer `j` starting from index 2. For each element `nums[j]`, we compare it with `nums[i - 2]`. If they are different, it means we haven't yet placed two copies of this element in our reconstructed array, so we copy `nums[j]` to `nums[i]` and increment `i`. If they are the same, we skip `nums[j]` as it would exceed the limit of two duplicates.

### Code
```py
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        i = 2
        for j in range(2, len(nums)):
            if nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1
        return i
```
