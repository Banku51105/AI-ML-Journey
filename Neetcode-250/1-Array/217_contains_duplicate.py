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
def test_has_duplicate():
    sol = Solution()
    assert sol.hasDuplicate([1, 2, 3, 1]) is True
    assert sol.hasDuplicate([1, 2, 3, 4]) is False
    assert sol.hasDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    assert sol.hasDuplicate([]) is False
if __name__ == "__main__":
    test_has_duplicate()
    print("All tests passed.")