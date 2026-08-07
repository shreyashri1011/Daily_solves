class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        hashmap= {')':'(' , '}':'{', ']':'['}
        for element in s:
            if stack and (element in hashmap and stack[-1] == hashmap[element]):
                stack.pop()
            else:
                stack.append(element)
        return not stack