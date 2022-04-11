'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

"""
@param: strs: a list of strings
@return: encodes a list of strings to a single string.
"""
def encode(strs):
  """
  We take in a list of strings measure a the length of each string and encode the length with a delimiter to allow for the decoder to work
  """
    # write your code here
    s=""
    for i in strs:
        x = len(i)
        s += str(x) + "#" + i
    return s

"""
@param: str: A string
@return: dcodes a single string to a list of strings
"""
def decode(strs):
  """
  Take the string and take in the entire number first which will be everything except the first delimiter. Convert that number to an integer and then 
  take everything after that delimiter and make it a string in your output and then repeat for the rest of the string!
  """
    # write your code here
    ans,i = [],0
    
    while i < len(strs):
        j = i
        while strs[j] != "#":
            j +=1
        length = int(strs[i:j])
        ans.append(strs[j+1 : j+1+length])
        i = j + 1 + length
        
    return ans
