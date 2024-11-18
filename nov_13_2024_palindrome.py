# Given a string s, return the longest
# palindromic

# substring
#  in s.



# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"


# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

test = 'babad'
test2 = 'cbbd'
test3 = 'ac'

class Solution:
    def longestPalindrome(self, s: str) -> str:
        temp_list = []

        # inputting idx of str and characters into list of tuples
        for idx, val in enumerate(s):
            temp_list.append((val, idx))

        # print(temp_list, "temp_list")

        idx_counter = 0

        # number of characters that are similar between the two lists
        char_counter = 0
        palindrome_idx_list = []

        # compare them and see where they overlap!
        for i in reversed(range(len(s))):
            # finding beginning of palindrome
            if (s[i] == temp_list[idx_counter][0]):
                char_counter +=1
                palindrome_idx_list.append(idx_counter)
                idx_counter += 1
            else:
                char_counter = 0
                idx_counter += 1

        if len(palindrome_idx_list) > 1:
            final = s[palindrome_idx_list[0]:palindrome_idx_list[-1] + 1]
        else:
            final = s[0]

        return final


#need to figure out whwat to do for the test case "abb"

s1 = Solution()
print(s1.longestPalindrome(test3))

        # print(s, "start string")

        final = s[palindrome_idx_list[0]:palindrome_idx_list[-1]+1]
        # print(final)

        return final

s1 = Solution()
print(s1.longestPalindrome(test2))

