class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry=0
        for i in range(len(digits)-1,-1,-1):
            if digits[i]!=9 and i==len(digits)-1:
                digits[i]=digits[i]+1
                return digits
            elif digits[i]==9 and i!=0:
                carry=1
                digits[i]=0
            elif digits[i]!=9 and i!=len(digits)-1:
                digits[i]=digits[i]+carry
                return digits
            elif digits[i]==9 and i==0:
                digits[i]=1
                digits.append(0)
                return digits
        
        
        return digits