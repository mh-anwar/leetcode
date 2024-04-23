#  3121. Count the Number of Special Characters II (Contest 394)
# 2024-04-21

# Approach
# 

# Complexity
# Time: O(n)
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # keep track of the lowercase
        # while checking if an uppercase appears
        occurences = {}
        special = 0
        # print(word)
        for i in word:
            # print(occurences)
            if i.islower() and i in occurences: 
                # print(i + ": " + str(occurences[i]["upper"]))
                if occurences[i]["upper"] == True and occurences[i]["lower"] == True:
                    occurences[i]["lower"] = False
                    print(str(i) + ' doesnt count ' + str(special) )
                    special -= 1
            elif i.islower() and i not in occurences:
                occurences[i] = {"lower": True, "upper": False, "dbl": False}
            elif i.lower() in occurences:
                if occurences[i.lower()]["upper"] == False and occurences[i.lower()]["dbl"] == False:
                    occurences[i.lower()]["upper"] = True
                    special += 1
            else:
                occurences[i.lower()] = {"lower": True, "upper": False, "dbl": True}
        return special