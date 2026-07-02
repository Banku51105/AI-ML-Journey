# LeetCode 217 - Contains Duplicate
# Pattern: Hash Set / Seen Elements

# Idea:
# Keep track of numbers we've already seen.
# If a number appears again, return True immediately.

# Time Complexity: O(n)
# Space Complexity: O(n)

# Key Takeaway:
# Hash Sets provide O(1) average lookup time.
# When a problem asks whether an element has appeared before,
# a Hash Set is often the first tool to consider.

# Solution:
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False