"""
This is a straight forward implementation and use case of a Segment Tree.
The main idea is that you make an array of size 2n where n is the size of the input array
and that new array will be a tree like array of partial sums of the input array. As an example of an additive segment tree,
SegmentTree([1,2,3,4]) -> [0,10,3,7,1,2,3,4]
As a note the 0th entry will always be 0 here since we're considering the 1st entry the root of the segment tree.
Other things to note, the original array is placed in positions [n:2n] as they are the base of the tree and we're following the convention that
child nodes are in position 2n and 2n+1 from the parent node. After filling in the base, we then fill in the rest of the Tree by calling the operation 
for index i on children 2i and 2i+1. 

In the above example you can see that for indices 1-(n-1) (or 1-3 in this case) we have the relation that i = (2i) operation (2i+1), for instance:

7 (index 3) = 3 (index 6) + 4 (index 7)
3 (index 2) = 1 (index 4) + 2 (index 5)
10 (index 1) = 3 (index 2) + 7 (index 3)

For updating, we update the index i in the base of the tree which is index n+i and then we update all the parents which should be i//2 and so on
so we call the operation for all the parent nodes.

For querying, we need to write a bit more code since we calculate partial sums for halves quarters and such but we don't precompute off set intervals like (1-3)
and such so we need to accumulate results from the left which would just be the value of 1 in our example then accumulate from the right which would be 2-3 in the example.

As a note, our implementation goes from [left,right) so we're excluding the index to the right.
Thus to accumulate, we start with our identity and our left and right pointers in the base of the tree and then move inwards. 
To do so, we loop while the left pointer is less than the right one, we do ops when the index of the pointers are odd to pick up any straglers and we do 
ops between our accumulator and the value the pointers are at.
Then we move the left and right pointers inwards which means an increment and decrement respectively. Finally we always divided by 2 to go to their parent nodes
and in the end we return the result of the op of the accumulated left and right fields.
"""
class SegmentTree:
    def __init__(self, nums, op= lambda a,b: a+b, identity=0):
        self.n = len(nums)
        self.op = op
        self.identity = identity

        self.tree = [identity] * (2*self.n)

        for i in range(self.n):
            self.tree[self.n+i] = nums[i]
        
        for i in range(self.n-1,0,-1):
            self.tree[i] = self.op(self.tree[2*i], self.tree[2*i+1])

    def update(self, index, number):
        i = self.n + index
        self.tree[i] = number

        i = i //2

        while i:
            self.tree[i] = self.op(self.tree[2*i], self.tree[2*i+1])
            i = i //2

    def query(self, left_index, excluded_right_index):
        left_index += self.n
        excluded_right_index += self.n
        result_left = self.identity
        result_right = self.identity

        while left_index < excluded_right_index:
            if left_index % 2 ==1:
                result_left = self.op(result_left, self.tree[left_index])
                left_index +=1
            
            if excluded_right_index % 2 ==1:
                excluded_right_index -=1
                result_right = self.op( self.tree[excluded_right_index], result_right)
            
            left_index = left_index//2
            excluded_right_index = excluded_right_index //2

        return self.op(result_left, result_right)
            

class NumArray:

    def __init__(self, nums: list[int]):
        self.tree = SegmentTree(nums)
        

    def update(self, index: int, val: int) -> None:
        self.tree.update(index, val)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.query(left, right+1)
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
