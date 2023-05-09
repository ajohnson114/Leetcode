def plusOne(self, digits: List[int]) -> List[int]:
  """
  I think this is a custom solution of mine. The basic idea is to sort of decompose the digits list into the ones, tens, hundreds, etc. column
  then add them all into a concrete number. After we do that we add one to that number and then we turn that number into a string in python and
  then iterate through the string to add each element to a list while converting it to an integer for the answer.
  
  Basic idea: Input: [1,2,3,4] -function-> num = 0 -> num += 1000+200+30+4 -> num = str(num) -return-> [int(i) for i in num] Q.E.D
  """
        num = 0
        for i,a in enumerate(digits):
            num += (10 ** i) * digits[~i]
        num +=1
        ans = []
        for i in str(num):
            ans.append(int(i))
        return ans
