"""
This question gives us a number line starting at 0 and two kinds of queries. [1, x] puts an obstacle at x, and [2, x, sz] asks
whether a block of length sz can fit somewhere inside [0, x] without overlapping an obstacle (touching one is fine).
So for a type 2 query we really want the biggest empty gap inside [0, x] and check if it is >= sz.

The way to think about it is that the obstacles (plus a fake one at 0 for the left wall) chop the line into gaps, and each gap
ends at an obstacle. So we store each gap at the position of the obstacle on its RIGHT: tree[pos] = pos - previous obstacle.
Then the tree is a max segment tree over positions (see RangeSumQuery.py for how the tree works, here op = max and identity = 0
which is fine since gaps are never negative). Positions are bounded by the biggest x in the queries, so we size the tree from
that and index it by position directly with no compression needed. A SortedList of obstacle positions lets us find the
neighbors of any x in O(log n).

Placing an obstacle at x splits the gap between its neighbors prev < x < nxt into two:
the new gap ending at x is x - prev, and the gap ending at nxt shrinks from nxt - prev to nxt - x.
So that is two point updates. The shrinking one is why update has to SET the value and rebuild the parents from their children,
a max tree that only ever "maxes in" a new value would keep the old bigger gap around.

For [2, x, sz] let prev be the last obstacle <= x. Every gap ending at an obstacle in [0, prev] lies fully inside [0, x],
so tree.query(0, prev + 1) gives the best of those. The gap after prev is only partly inside [0, x] since the next obstacle
might be past x, so we only get to use the piece x - prev. The answer is max(those two) >= sz.

As an example, queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]] (answer is [True, True, False]):
size = 8, obstacles = [0], all gaps 0
[1,7]:   prev=0, no nxt                 -> gap[7] = 7                     obstacles [0,7]
[2,7,6]: prev=7, query [0,8) = 7, tail 7-7 = 0 -> best 7 >= 6         True
[1,2]:   prev=0, nxt=7                  -> gap[2] = 2, gap[7] shrinks to 5  obstacles [0,2,7]
[2,7,5]: prev=7, query [0,8) = max(2,5) = 5, tail 0 -> 5 >= 5         True
[2,7,6]: same best of 5 -> 5 >= 6                                      False

Things to remember:
Start obstacles with 0, it acts as the left wall so prev always exists (x >= 1 so obstacles[idx - 1] is safe).
The gap lives at the obstacle on its right, so when inserting x you update BOTH x and the next obstacle.
For the type 2 query use bisect_right so an obstacle sitting exactly at x counts as prev (then the tail is 0).
Query the tree up to prev + 1, NOT x + 1, because the gap ending at the next obstacle can stick out past x.
It is >= sz not > sz since the block can touch obstacles and the ends of the range.
sortedcontainers isn't in the standard library (LeetCode has it). If an interviewer doesn't allow it, prev can be found with
another max segment tree that stores pos at each obstacle position: query(0, x + 1) gives the last obstacle <= x
(and a min tree finds the next one).
Time is O(q log M) where M is the biggest x, space is O(M + q).
"""

from typing import List
from sortedcontainers import SortedList


class SegmentTree:
    def __init__(self, nums, op=lambda a, b: a + b, identity=0):
        self.n = len(nums)
        self.op = op
        self.identity = identity
        self.tree = [self.identity] * (self.n * 2)

        for i in range(self.n):
            self.tree[i + self.n] = nums[i]
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


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        size = max(q[1] for q in queries) + 1
        tree = SegmentTree([0] * size, op=max, identity=0)
        obstacles = SortedList([0])
        ans = []

        for q in queries:
            x = q[1]
            if q[0] == 1:
                idx = obstacles.bisect_left(x)
                prev = obstacles[idx - 1]
                tree.update(x, x - prev)              # new gap ending at x
                if idx < len(obstacles):
                    nxt = obstacles[idx]
                    tree.update(nxt, nxt - x)         # gap ending at nxt shrinks
                obstacles.add(x)
            else:
                sz = q[2]
                prev = obstacles[obstacles.bisect_right(x) - 1]
                best = max(tree.query(0, prev + 1), x - prev)
                ans.append(best >= sz)

        return ans
