"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""
"""
We know that the celebrity doesn't know any one in the party. So we know that if the candidate we're looking at knows someone the person they're looking at
might be the celebrity but the person looking isn't. So we can look through all the people and check this. Then we can check if when the person is looking
at someone else and they know them we should return -1 or if someone doesn't know the candidate we should return -1 as well. If we can pass this check then
we can return -1. If we pass all of this then we can return the candidate.
"""

class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        # Write your code here
        candidate = 0
        for i in range(n):
            if knows(candidate,i):
                candidate = i

        for i in range(n):
            if (i != candidate and knows(candidate,i)) or not knows(i,candidate):
                return -1
        
        return candidate
