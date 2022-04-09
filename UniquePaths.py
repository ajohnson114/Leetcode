def uniquePaths(self, m, n):
	"""
	The way to look at this problem is that the person is standing on a grid already so he doesn't have to take that grid into account (aka each direction
	will have 1 less step that needs to be taken at first glance) and he has to choose when he will move down (or right it's the same thing). The simplest
	way to visualize this is to write out the decision. Take the 2x2 case he's already at (1,1) so he can either do DR or RD. In this example, he has to 
	take 2 steps and 1 of them needs to be down so he has the choose when which leads to our combinatorial understanding of nCr. Picture all the steps
	out in a line DRDDRDRDRDRRDR for instance you will need to choose where to place the D's (or R's). Therefore, the answer to this will be 
	(m = total_amount_of_steps_taken n = steps_right) mCn. Looking at my solution again I think you don't need the max and min functions but at the time
	I tried a different version of code that gave me some trouble
	"""
	
	"""
	:type m: int
	:type n: int
	:rtype: int
	"""

	def factorial(n):
		ans = 1
		for i in range(1,n+1):
			ans *= i
		return ans

	def comb(m,n):
		return factorial(m)/(factorial(n)*factorial(m-n))

	big = max(m,n)
	small = min(m,n)
	return comb(big + small - 2,small-1)
