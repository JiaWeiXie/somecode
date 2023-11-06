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
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        length = len(s)
        left = 0
        right = 0
        mini_window = ""
        while left < length:
            tmp = t
            flag = False
            while tmp and right < length:
                char = s[right]
                print(char, end="")
                if char in tmp:
                    tmp = tmp.replace(char, "", 1)
                    if not flag:
                        flag = True
                        left = right
                
                string = s[left:right+1]
                if not tmp and (mini_window == "" or len(string) < len(mini_window)):
                    mini_window = string
                right += 1
            print()
            left += 1
            right = left
        return mini_window

solution = Solution()
with open("76/in.txt", "r", encoding="utf-8") as input_file:
    for line in input_file.read().splitlines():
        s, t , *_ = line.split(",")
        print("=" * 20, s, "=" * 20)
        print(solution.minWindow(s, t))                     
                
                
                
                
            
        