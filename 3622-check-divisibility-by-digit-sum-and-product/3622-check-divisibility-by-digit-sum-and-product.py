class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum1=0
        b=n
        prod=1
        while b>0:
            sum1+=b%10
            prod*=b%10
            b//=10
        return n%(sum1+prod)==0
        