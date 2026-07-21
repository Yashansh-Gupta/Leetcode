class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        q=[]
        for i in s:
            if i.isalpha() or i.isdigit():
                if i.isalpha():
                    i=i.lower()
                q.append(i)
        
        if q==q[::-1]:
            return True
        else:
            return False
            