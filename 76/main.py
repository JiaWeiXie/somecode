"""
76. Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window
substring
of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.


Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:
m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""

from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0
        mini_window = ""
        counter = dict(Counter(t))
        cnt = defaultdict(lambda: 0)

        def check():
            for k, v in counter.items():
                if cnt[k] < v:
                    return False
            return True

        for right, char in enumerate(s):
            if char in counter:
                cnt[char] += 1

            while check():
                substring = s[left : right + 1]
                if len(substring) <= len(mini_window) or mini_window == "":
                    mini_window = substring

                if s[left] in cnt:
                    cnt[s[left]] -= 1
                left += 1

        return mini_window


from pathlib import Path

solution = Solution()
with Path("76/in.txt").open(encoding="utf-8") as input_file:
    for line in input_file.read().splitlines():
        s, t, *_ = line.split(",")
        print("=" * 20, s, "=" * 20, t, "=" * 20)
        print(solution.minWindow(s, t))
