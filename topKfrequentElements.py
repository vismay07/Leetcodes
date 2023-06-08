# 347. Top K Frequent Elements
# Medium
# 14.5K
# 511
# Companies
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]


# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.


# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        counter = 1
        steps = 0
        players = list(range(1, n + 1))
        scores = dict()
        for i in players:
            scores[i] = 0
        i = 1
        while True:
            # print(i)
            if scores[i] != 1:
                scores[i] += 1
            else:
                j = 1
                while j < n + 1:
                    print(f"{j}=> {scores[j]}")
                    if scores[j] == 1:
                        print(j)
                        players.remove(j)
                    j += 1
                return players
            # print(scores)
            steps = i + (counter * k)
            if steps > n:
                steps = abs(steps - n)
                while steps > n:
                    steps = abs(steps - n)
                i = steps
            else:
                i = steps
            counter += 1

