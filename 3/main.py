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
        max_index = len(s) - 1
        offset = 0
        index = 0
        substring = ""
        longest = ""
        while offset <= max_index:
            char = s[index]
            if char in substring:
                offset += 1
                index = offset
                substring = ""
            else:
                substring += char
                index += 1

            if len(substring) > len(longest):
                longest = substring

            if index > max_index:
                offset += len(longest)
                index = offset
                substring = ""
                continue

        return len(longest)


from pathlib import Path

solution = Solution()
with Path("3/in.txt").open(encoding="utf-8") as input_file:
    for line in input_file.read().splitlines():
        print("=" * 20)
        print(solution.lengthOfLongestSubstring(line))
