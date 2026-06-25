# LeetCode 14 - Longest Common Prefix
# Pattern: Vertical Scanning

# Idea:
# Compare characters column by column using the first string as reference.
# Stop on the first mismatch or when a string ends.

# Time: O(n × m)
# Space: O(1)

# Key Takeaway:
# Scan vertically instead of comparing every pair of strings.

# Solution:
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common = strs[0]
        lcp = ""
        for i in range(len(common)):
            for j in range(1, len(strs)):
                if i < len(strs[j]):
                    if common[i] != strs[j][i]:
                        return lcp
                else:
                    return lcp
            lcp += common[i]
        return lcp
def test_longest_common_prefix():
    sol = Solution()
    assert sol.longestCommonPrefix(["bat", "bag", "bank", "band"]) == "ba"
    assert sol.longestCommonPrefix(["dance", "dag", "danger", "damage"]) == "da"
    assert sol.longestCommonPrefix(["neet", "feet"]) == ""
if __name__ == "__main__":
    test_longest_common_prefix()
    print("All tests passed.")