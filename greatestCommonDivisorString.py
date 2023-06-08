#  Greatest Common Divisor of Strings
# Easy
# 3.5K
# 571
# Companies
# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.


# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""


# Constraints:

# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        divisor = ""
        str_op = ""
        flag = 0
        if len(str1) < len(str2):
            divisor = str1
            max_len = len(str2)
        else:
            divisor = str2
            max_len = len(str1)
        i = 1
        while len(divisor) != 0:
            # print(f'Divisor: {divisor}, String1: {str1}, String2: {str2}')
            if divisor * i == str1:
                # print("ello")
                flag += 1
            if divisor * i == str2:
                # print("mello")
                flag += 1
            if flag == 2:
                str_op = divisor
                # print(f'Expected Output: {str_op}')
                break
            if len(divisor) * i > max_len:
                divisor = divisor[: len(divisor) - 1 :]
                i = 1
                flag = 0
            i += 1
        return str_op

