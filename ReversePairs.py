"""
This question asks us to count the pairs (i, j) where i < j and nums[i] > 2*nums[j]. Whenever a question asks to count pairs
i < j that satisfy some condition between nums[i] and nums[j], the trick is to sweep left to right and keep a structure that
remembers everything we've seen so far. Then for each new number y we ask "how many earlier numbers x satisfy the condition?"
and afterwards we add y to the structure. Here the structure is a segment tree of counts (see RangeSumQuery.py for how the
segment tree itself works, this file just uses it).

The segment tree is indexed by value, not by position in nums, so tree leaf k holds how many times we've seen the k-th smallest value.
Since the values can be huge or negative we can't index by them directly, so we do coordinate compression: collect the values,
sort them, and map each one to its rank (0, 1, 2, ...). The important detail is that we compress every x AND every 2*x, because
2*y is used as the boundary in our query and it needs its own rank even if it never shows up in nums.

Then for each y the earlier x's with x > 2*y are exactly the ones whose rank is strictly bigger than rank[2*y], so we query
[rank[2*y]+1, len(vals)) (right side excluded like usual). After that we increment the count at rank[y].

As an example, nums = [1,3,2,3,1] (answer is 2):
values we need = {1,3,2} plus doubles {2,6,4} -> vals = [1,2,3,4,6] so rank = {1:0, 2:1, 3:2, 4:3, 6:4}
y=1: query ranks > rank[2]=1 -> 0 seen so far,                  add 1 -> counts [1,0,0,0,0]
y=3: query ranks > rank[6]=4 -> empty range, 0,                  add 3 -> counts [1,0,1,0,0]
y=2: query ranks > rank[4]=3 -> 0,                               add 2 -> counts [1,1,1,0,0]
y=3: query ranks > rank[6]=4 -> 0,                               add 3 -> counts [1,1,2,0,0]
y=1: query ranks > rank[2]=1 -> ranks 2,3,4 -> 2+0+0 = 2,        add 1
total = 2, which are the two (3, 1) pairs.

Things to remember:
We query BEFORE we insert y. That is what makes it i < j, and it also matters for negatives since y = -1 satisfies -1 > -2,
so inserting first would count y pairing with itself.
We forget to compress 2*x -> KeyError on rank[2*y].
The increment reads the current leaf value tree.tree[r + tree.n] and writes back +1 since update sets a value rather than adding.
In query the right accumulator is op(tree[right], right_result) so the order is preserved if op isn't commutative (doesn't matter for sums).
Time is O(n log n) for the sort plus n queries/updates, space is O(n). The other well known way to do this is merge sort counting.
"""

class SegmentTree:
    def __init__(self, nums, op=lambda a, b: a + b, identity=0):
        self.n = len(nums)
        self.op = op
        self.identity = identity

        self.tree = [self.identity] * (2 * self.n)

        for i in range(self.n):
            self.tree[i + self.n] = nums[i]

        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.op(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, index, value):
        i = index + self.n
        self.tree[i] = value

        i //= 2
        while i:
            self.tree[i] = self.op(self.tree[2 * i], self.tree[2 * i + 1])
            i //= 2

    def query(self, left_index, excluded_right_index):
        left_index += self.n
        excluded_right_index += self.n
        left_result = right_result = self.identity

        while left_index < excluded_right_index:
            if left_index % 2 == 1:
                left_result = self.op(left_result, self.tree[left_index])
                left_index += 1

            if excluded_right_index % 2 == 1:
                excluded_right_index -= 1
                right_result = self.op(self.tree[excluded_right_index], right_result)

            left_index //= 2
            excluded_right_index //= 2

        return self.op(left_result, right_result)


class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        if not nums:
            return 0

        # Compress every value we'll store (x) or use as a boundary (2*y)
        all_values = set()
        for x in nums:
            all_values.add(x)
            all_values.add(2 * x)
        vals = sorted(all_values)
        rank = {v: i for i, v in enumerate(vals)}
        tree = SegmentTree([0] * len(vals))

        ans = 0
        for y in nums:
            # Count earlier x with x > 2*y: ranks strictly above rank[2*y]
            ans += tree.query(rank[2 * y] + 1, len(vals))

            r = rank[y]
            tree.update(r, tree.tree[r + tree.n] + 1)

        return ans
