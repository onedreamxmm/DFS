'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.

time complexity: O(n!)
space complexity: O(n!)
'''

class Solution:
    def permutation1(self, nums):
        def dfs(nums, path):
            if not nums:
                return res.append(path)
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], path+[nums[i]])

        res = []
        dfs(nums, [])
        return res


    def permutation2(self, nums):
        def backtrack(first):
            if first == n-1:
                return res.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first+1)
                nums[first], nums[i] = nums[i], nums[first]

        res = []
        n = len(nums)
        backtrack(0)
        return res