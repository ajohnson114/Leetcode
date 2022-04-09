def bulbSwitch(self, n: int) -> int:
  """This is a math trick problem. Where the bulb of square numbers will be left on"""
        count = 0
        i = 1
        while i**2 <= n:
            i += 1
            count += 1
        return count
