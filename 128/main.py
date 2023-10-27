"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, 
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        values = set(nums)
        longest = 1
        tmp = values.pop()
        tmp_val = 1
        while values:
            if tmp - 1 in values:
                values.add(tmp)
                tmp -= 1
                values.remove(tmp)
                continue

            if tmp + 1 in values:
                tmp += 1
                tmp_val += 1
                values.remove(tmp)
            else:
                tmp = values.pop()
                tmp_val = 1
            longest = max(longest, tmp_val)

        return longest


import json

solution = Solution()
with open("128/in.txt", "r", encoding="utf-8") as input_file:
    for line in input_file.read().splitlines():
        nums = json.loads(line)
        print(solution.longestConsecutive(nums))
