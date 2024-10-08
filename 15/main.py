"""
15. 3Sum

Given an integer array nums,
return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k,
and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

from collections import defaultdict


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = set()
        nums = sorted(nums)
        count = len(nums)
        counter = defaultdict(lambda: 0)
        for v in nums:
            counter[v] += 1

        for i in range(0, count - 1):
            x = nums[i]
            counter[x] -= 1
            tmp_counter = counter.copy()
            for j in range(i + 1, count):
                y = nums[j]
                tmp_counter[y] -= 1
                t = -(x + y)
                if tmp_counter[t] > 0 and t >= y:
                    result.add((x, y, t))
                    tmp_counter[t] -= 1
        return list(map(list, result))


import json
from pathlib import Path

solution = Solution()
with Path("15/in.txt").open(encoding="utf-8") as input_file:
    for line in input_file.read().splitlines():
        strs = json.loads(line)
        print(solution.threeSum(strs))
