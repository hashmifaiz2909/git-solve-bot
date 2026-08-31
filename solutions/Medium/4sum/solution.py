class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        results = []
        
        for i in range(n - 3):
            # Avoid duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Optimization: if the smallest possible sum is greater than target, break
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            # Optimization: if the largest possible sum with nums[i] is less than target, skip
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue
                
            for j in range(i + 1, n - 2):
                # Avoid duplicates for the second element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # Optimization: if the smallest possible sum is greater than target, break
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                # Optimization: if the largest possible sum with nums[i] and nums[j] is less than target, skip
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue
                
                # Two-pointer approach for the remaining two elements
                left, right = j + 1, n - 1
                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if curr_sum == target:
                        results.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        # Avoid duplicates for the third element
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        # Avoid duplicates for the fourth element
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif curr_sum < target:
                        left += 1
                    else:
                        right -= 1
                        
        return results
