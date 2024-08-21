"""
238. Product of Array Except Self

Given an integer array nums,
return an array answer such that answer[i] is equal
to the product of all the elements olinef nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time
and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        product = 1
        count = len(nums)
        for idx in range(0, count):
            result.append(product)
            product *= nums[idx]

        product = 1
        for idx in range(count - 1, -1, -1):
            result[idx] *= product
            product *= nums[idx]

        return result


import json
from pathlib import Path

solution = Solution()
with Path("238/in.txt").open(encoding="utf-8") as input_file:
    for line in input_file.read().splitlines():
        nums = json.loads(line)
        print(solution.productExceptSelf(nums))
