# Search in Rotated Sorted Array
# Scenario: Find an element in a rotated sorted array.
# Task: Locate a target using modified binary search.
# Justification: Exploit sorted structure.
# Provide proof of Time Complexity: O(log n)

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2  
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
    
nums = [15, 18,1, 2, 3, 6, 12]
target = 3
rotatedArray  = Solution()
print("Target index ")
print(rotatedArray.search(nums, target))  # Output: 3