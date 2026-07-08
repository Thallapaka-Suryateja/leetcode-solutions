class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        n=x
        l=[]
        while n>0: 
            l.append(n%10)
            n//=10
        for i in range(len(l)//2):
            if l[i]!=l[-1-i]:
                return False
        return True