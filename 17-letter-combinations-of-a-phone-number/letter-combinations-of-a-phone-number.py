class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
            
        # Dictionary mapping digits to letters
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        result = []

        # Helper recursive function
        def solve(index, current_string):
            # Base Case: When the combined string length matches input length
            if index == len(digits):
                result.append(current_string)
                return
            
            # Fetch letters for current digit from dictionary
            current_digit = digits[index]
            letters = phone_map[current_digit]
            
            # Recurse for every possible letter
            for letter in letters:
                solve(index + 1, current_string + letter)

        # Start recursion at index 0 with an empty string
        solve(0, "")
        return result