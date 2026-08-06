class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        def func(n):
            b=1
            while n>0:
                b=b*(n%10)
                n=n//10
            return b
        while True:
            a=func(n)
            if a%t==0:
                return n
            n+=1
        