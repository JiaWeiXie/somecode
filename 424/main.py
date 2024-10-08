"""
424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = len(s)
        counter = defaultdict(lambda: 0)
        left = 0
        right = 0
        longest = 0
        while right < length:
            counter[s[right]] += 1
            while right - left + 1 - max(counter.values()) > k:
                counter[s[left]] -= 1
                left += 1

            longest = max(right - left + 1, longest)
            right += 1

        return longest


from pathlib import Path

solution = Solution()
with Path("424/in.txt").open(encoding="utf-8") as input_file:
    for line in input_file.read().splitlines():
        s, k = line.split(",")
        print("=" * 20, s, k)
        print(solution.characterReplacement(s, int(k)))
