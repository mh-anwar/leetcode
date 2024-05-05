# 100284. Valid Word (Contest 396)
# 2024-05-04

# Approach
# Match all constraints provided

class Solution:
    def isValid(self, word: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u']
        word = word.lower()
        if len(word) >= 3:
            vow = False
            conso = False
            if not word.isalnum():
                return False
            for i in word:
                if vow and conso:
                    break
                if i in vowels:
                    vow = True
                elif not i.isnumeric():
                    conso = True
            if not vow or not conso:
                return False
            return True
        return False