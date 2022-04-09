def trailingZeroes(self, n: int) -> int:
  """The key to understanding this is to understand the trick really. A 0 is made when a 5 and a 2 are multiplied together. Since there are factors of 2
  in each even number what we want to find out is the amount of 5's in the factorization of the number. Therefore, we initialize a counting variable and
  add the amount of times we can divide by 5 into that then divide the answer of that division by 5 until we can no longer divide by 5. This will take 
  out all factors of 5. For instance 125 // 5 = 25  25//5 = 5 5//5 = 1 1+5+25 = 31.  Theres 1 factor of 5 in each of the 25 multiples of 5 between 1 and 
  125, there's another factor of 5 in all multiples of 25 (25,50,75,100,125) and finally there's a 3rd factor of 5 in 125 (5**3 = 125). This gives us 
  our answer of 31!
  """
        count = 0
        while n >= 5:
            count += n//5
            n = n//5
        return count
