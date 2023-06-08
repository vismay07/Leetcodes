# 345. Reverse Vowels of a String
# Easy
# 3.5K
# 2.4K
# Companies
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"


# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        string_vowels = []
        count = 0
        for i in s:
            if i in vowels:
                string_vowels.append(i)
                count += 1
        print(string_vowels)
        for i in range(len(s)):
            if s[i] in vowels:
                # print(s[i])
                # print(s[:i:])
                s = s[:i:] + string_vowels[count - 1] + s[i + 1 : :]
                count -= 1
        return s
