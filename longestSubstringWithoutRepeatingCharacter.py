# 3. Longest Substring Without Repeating Characters
# Medium
# 34K
# 1.5K
# Companies
# Given a string s, find the length of the longest
# substring
#  without repeating characters.


# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = i
        s_list = list(s)
        subs = ""
        len_subs = 0
        len_curr = 0
        curr_subs = ""
        if len(s_list) == 1:
            return 1
        while j < len(s_list):
            if s_list[j] not in curr_subs:
                curr_subs += s_list[j]
                len_curr += 1
                if len_curr > len_subs:
                    subs = curr_subs
                    len_subs = len_curr
            else:
                curr_subs = ""
                len_curr = 0
                i += 1
                j = i
            j += 1
            if len_curr == 0:
                j = i
            # print(curr_subs, len_curr)
            if j == len(s_list):
                i += 1
            if len(s_list) - i < len_subs:
                return len_subs
        # print(f"subs:{subs}, len:{len_subs}")
        return len_subs

