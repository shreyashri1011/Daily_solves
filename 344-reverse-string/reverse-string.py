class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None
        """

        stack = []

        # Push all characters into stack
        for ch in s:
            stack.append(ch)

        # Pop and put back into s
        for i in range(len(s)):
            s[i] = stack.pop()