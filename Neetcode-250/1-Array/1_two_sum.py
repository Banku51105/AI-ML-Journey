# LeetCode 1 - Two Sum
# Pattern: Brute Force Pair Search

# Idea:
# Check every possible pair of numbers.
# If their sum equals target, return their indices.

# Time Complexity: O(n²)
# Space Complexity: O(1)

# Key Takeaway:
# This brute-force solution works but is inefficient.
# The important insight is:
# needed_number = target - current_number
# This observation leads to the optimal Hash Map solution.

# Solution:
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
def test_two_sum():
    sol = Solution()
    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert sol.twoSum([3, 2, 4], 6) == [1, 2]
    assert sol.twoSum([3, 3], 6) == [0, 1]
if __name__ == "__main__":
    test_two_sum()
    print("All tests passed.")