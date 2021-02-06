'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]

'''

class Solution:
    def generateParenthesis(self, n):
        def dfs(i, path, l, r):
            if i == 2*n:
                return res.append(path)
            if l < n:
                dfs(i+1, path+'(', l+1, r)
            if r < l:
                dfs(i+1, path+')', l, r+1)
        if not n:
            return 'No well-formed parentheses'
        res = []
        dfs(0, '', 0, 0)
        return res

if __name__ == '__main__':
    o = Solution()
    print(o.generateParenthesis(0))
    print(o.generateParenthesis(1))
    print(o.generateParenthesis(2))
    print(o.generateParenthesis(3))

