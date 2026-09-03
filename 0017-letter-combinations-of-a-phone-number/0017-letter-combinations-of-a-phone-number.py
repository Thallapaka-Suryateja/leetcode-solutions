class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dictt = {
            "2": ("a", "b", "c"),
            "3": ("d", "e", "f"),
            "4": ("g", "h", "i"),
            "5": ("j", "k", "l"),
            "6": ("m", "n", "o"),
            "7": ("p", "q", "r", "s"),
            "8": ("t", "u", "v"),
            "9": ("w", "x", "y", "z"),
        }

        if not digits:
            return []

        result = [""]

        for digit in digits:
            new_result = []

            for combination in result:
                for letter in dictt[digit]:
                    new_result.append(combination + letter)

            result = new_result

        return result