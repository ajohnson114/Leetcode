"""
This question asks us to count the subarrays whose sum lands in [lower, upper]. The first step is to turn subarray sums into
something about pairs, which we do with prefix sums. With prefix[0] = 0 and prefix[k+1] = prefix[k] + nums[k], the sum of
nums[i..j] is prefix[j+1] - prefix[i]. So we want to count pairs i < j of prefix values with
lower <= prefix[j] - prefix[i] <= upper, and flipping that around to be about the earlier one gives
prefix[j] - upper <= prefix[i] <= prefix[j] - lower.

Now it is the same "count pairs i < j" pattern as ReversePairs.py: sweep the prefix array left to right, and for each prefix p
count how many earlier prefixes fall in the window [p - upper, p - lower], then add p to the structure. The structure is a
segment tree of counts indexed by the rank of the prefix value (see RangeSumQuery.py for how the tree works). I added an add
method to the tree so incrementing a count is tree.add(r, 1) instead of reading the leaf and writing it back.

The difference from ReversePairs is how we handle the window boundaries. There we compressed 2*x so the boundary always had a
rank. Here we only compress the prefix values themselves and find the boundaries with binary search on the sorted values:
bisect_left(values, p - upper) is the first rank whose value is >= p - upper (inclusive left end)
bisect_right(values, p - lower) is the first rank whose value is > p - lower, which is exactly the excluded right end our query wants.
So tree.query(lo, hi) counts every earlier prefix in the window, and if the window holds no values then lo == hi and we get 0.

As an example, nums = [-2,5,-1], lower = -2, upper = 2 (answer is 3):
prefix = [0,-2,3,2] -> values = [-2,0,2,3] so rank = {-2:0, 0:1, 2:2, 3:3}
p=0:  window [-2,2] -> lo=0, hi=3, query [0,3) = 0 (nothing seen yet),      add 0  -> counts [0,1,0,0]
p=-2: window [-4,0] -> lo=0, hi=2, query [0,2) = 0+1 = 1 (subarray [-2]),    add -2 -> counts [1,1,0,0]
p=3:  window [1,5]  -> lo=2, hi=4, query [2,4) = 0,                          add 3  -> counts [1,1,0,1]
p=2:  window [0,4]  -> lo=1, hi=4, query [1,4) = 1+0+1 = 2,                  add 2
      (the earlier 0 gives the whole array, sum 2, and the earlier 3 gives [-1])
total = 3.

Things to remember:
Prefix has len(nums)+1 entries and starts with 0, otherwise we miss every subarray that starts at index 0.
We query BEFORE we add p. That is what makes it i < j, and if lower <= 0 <= upper adding first would count p - p = 0,
which is the empty subarray and isn't allowed.
The window is about the EARLIER prefix, so it is [p - upper, p - lower] (upper on the left), easy to flip by accident.
bisect_left for the inclusive left end, bisect_right for the excluded right end, which lines up with the [left, right) query.
Time is O(n log n) for the sort plus n bisects/queries/adds, space is O(n). Merge sort counting is the other well known way.
"""

from bisect import bisect_left, bisect_right


class SegmentTree:
    def __init__(self, nums, op=lambda a, b: a + b, identity=0):
        self.n = len(nums)
        self.op = op
        self.identity = identity

        self.tree = [identity] * (self.n * 2)

        for i in range(self.n):
            self.tree[self.n + i] = nums[i]

        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.op(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, index, value):
        index += self.n
        self.tree[index] = value

        index //= 2

        while index:
            self.tree[index] = self.op(self.tree[2 * index], self.tree[2 * index + 1])
            index //= 2

    def query(self, left_index, excluded_right_index):
        left_index += self.n
        excluded_right_index += self.n
        left_accumulation = right_accumulation = self.identity

        while left_index < excluded_right_index:
            if left_index % 2 == 1:
                left_accumulation = self.op(left_accumulation, self.tree[left_index])
                left_index += 1
            if excluded_right_index % 2 == 1:
                excluded_right_index -= 1
                right_accumulation = self.op(self.tree[excluded_right_index], right_accumulation)
            left_index //= 2
            excluded_right_index //= 2
        return self.op(left_accumulation, right_accumulation)

    def add(self, index, delta):
        self.update(index, self.tree[index + self.n] + delta)


class Solution:
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        prefix = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            prefix[i + 1] = prefix[i] + x

        values = sorted(set(prefix))
        rank = {v: i for i, v in enumerate(values)}
        tree = SegmentTree([0] * len(values))

        count = 0
        for p in prefix:
            lo = bisect_left(values, p - upper)
            hi = bisect_right(values, p - lower)
            count += tree.query(lo, hi)
            r = rank[p]
            tree.add(r, 1)
        return count
