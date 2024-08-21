"""
11. Container With Most Water

You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container,
such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1


Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = -1
        max_value = 0
        max_width = len(height)
        while left < max_width and right > -max_width:
            left_height = height[left]
            right_height = height[right]
            width = max_width + right - left
            height_ = min(left_height, right_height)
            area = width * height_
            max_value = max(area, max_value)
            if left_height > right_height:
                right -= 1
            else:
                left += 1

        return max_value


import json
from pathlib import Path

solution = Solution()
with Path("11/in.txt").open(encoding="utf-8") as input_file:
    for line in input_file.read().splitlines():
        height = json.loads(line)
        print(solution.maxArea(height))
