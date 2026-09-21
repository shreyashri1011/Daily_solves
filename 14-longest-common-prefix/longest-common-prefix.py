class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # Take the first string as the base reference
        prefix = strs[0]
        
        for s in strs[1:]:
            # Shorten the prefix until s starts with it
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
                    
        return prefix