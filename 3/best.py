"""
3. Longest Substring Without Repeating Characters

Given a string `s`, find the length of the longest
substring without repeating characters.


Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3

Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        char_offset = dict()
        for right, char in enumerate(s):
            if char in char_offset and char_offset[char] >= left:
                left = char_offset[char] + 1

            char_offset[char] = right
            length = right - left + 1
            longest = max(length, longest)

        return longest


from pathlib import Path

solution = Solution()
with Path("3/in.txt").open(encoding="utf-8") as input_file:
    for line in input_file.read().splitlines():
        print("=" * 20)
        print(solution.lengthOfLongestSubstring(line))
