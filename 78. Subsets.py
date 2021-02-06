'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

'''


class Solution:
    def subsets1(self, nums):
        def dfs(i, path):
            if i == len(nums):
                return res.append(path)
            dfs(i+1, path+[nums[i]])
            dfs(i+1, path)
        res = []
        dfs(0, [])
        return res


    def subsets2(self, nums):
        subsets = [[]]
        for n in nums:
            subsets += [s + [n] for s in subsets]
        return subsets

    def subset3(self,nums):
        def dfs(nums, path=[]):
            res.append(path)
            for i in range(len(nums)):
                dfs(nums[i+1:], path+[nums[i]])
        res = []
        dfs()
        return res

if __name__ == '__main__':
    nums1 = []
    nums2 = [1, 2, 3]
    o = Solution()
    print(o.subsets1(nums1))
    print(o.subsets1(nums2))
    print(o.subsets2(nums1))
    print(o.subsets2(nums2))






