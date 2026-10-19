"""
Q: Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].

This is an additive segment tree question where what you want to store is the count of ranks of the numbers as they appear.
I'm taking it as a prerequisite that the reader's segment tree implementation is solid, if not look at https://github.com/ajohnson114/Leetcode/blob/main/RangeSumQuery.py
So you sort them and enumerate the sorted values and the sorted unique list of the values becomes the base of your segment tree.
You then traverse the original array backwards so that you're querying info for values to the right of your current index.
From there you get the rank of your current number, you then query the segment tree to see how many ranks between 0 and the current rank
have appeared before this one and append that to the output array for that index. You're going from right to left so that meets the constraints of the question.
From there, you update the segment tree to note that you've seen another instance of that rank and then move on. Since you're appending to an output array
you should just return that output array reversed since you filled it in in reverse.
"""

class SegmentTree:
    def __init__(self, nums, operation = lambda a,b: a+b, identity = 0):
        self.n = len(nums)
        self.identity = identity
        self.op = operation
        self.tree = [identity] * (self.n*2)

        for i in range(self.n):
            self.tree[i+self.n] = nums[i]

        for i in range(self.n-1,0,-1):
            self.tree[i] = self.op(self.tree[i*2], self.tree[2*i + 1])
    
    def update(self, index, value):
        i = index+self.n
        self.tree[i] = value

        i = i //2 

        while i:
            self.tree[i] = self.op(self.tree[2*i], self.tree[2*i+1])
            i = i //2
    
    def query(self, left_index, excluded_right_index):
        right_result, left_result = self.identity, self.identity
        left_ptr, right_ptr = left_index + self.n, excluded_right_index + self.n

        while left_ptr < right_ptr:
            if left_ptr %2 == 1:
                left_result = self.op(self.tree[left_ptr], left_result)
                left_ptr +=1
            
            if right_ptr %2 == 1:
                right_ptr -=1
                right_result = self.op(self.tree[right_ptr], right_result)

            right_ptr = right_ptr //2
            left_ptr = left_ptr //2
        
        return self.op(left_result, right_result)


class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        if not nums: return []

        vals = sorted(set(nums))
        rank = {x:i for i, x in enumerate(vals)}

        tree = SegmentTree([0]*len(vals))
        ans = []

        for x in reversed(nums):
            r = rank[x]
            ans.append(tree.query(0, r))
            tree.update(r, tree.query(r, r + 1) + 1)

        return ans[::-1]
