class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
            
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        result = []
        def solve(index,current_string):
            if index==len(digits):
                result.append(current_string)
                return
            current_digit=digits[index]
            letters=phone_map[current_digit]

            for letter in letters:
                solve(index+1,current_string+letter)
        solve(0,"")
        return result
        