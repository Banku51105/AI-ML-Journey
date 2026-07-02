# LeetCode 242 - Valid Anagram
# Pattern: Sorting / Frequency Counting

# Idea:
# Two strings are anagrams if they contain the same characters
# with the same frequencies.
# Sort both strings and compare them.

# Time Complexity: O(n log n)
# Space Complexity: O(n)

# Key Takeaway:
# Sorting can be used to compare character composition.
# A more optimal approach uses frequency counting (Hash Map)
# and runs in O(n) time.

# Solution:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)