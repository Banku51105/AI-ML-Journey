# LeetCode 1929 - Concatenation of Array
# Pattern: Array Traversal

# Idea:
# Traverse the array twice and append elements to a new list.

# Time Complexity: O(n)
# Space Complexity: O(n)

# Key Takeaway:
# Building a new array and understanding O(2n) = O(n).

# Solution:
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans
def test_get_concatenation():
    sol = Solution()
    assert sol.getConcatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]
    assert sol.getConcatenation([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]
    assert sol.getConcatenation([]) == []
if __name__ == "__main__":
    test_get_concatenation()
    print("All tests passed.")