'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

'''

class Solution:
    def permuteUnique(self, nums):
        def backtrack(path, counter):
            if len(path) == len(nums):
                return res.append(path)
            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    backtrack(path+[num], counter)
                    counter[num] += 1
        res = []
        backtrack([], Counter(nums))
        return res

