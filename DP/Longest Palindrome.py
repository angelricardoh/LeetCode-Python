class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s) # get length of input string
        result = s[0]

        dp = [[0 for _ in range(n)] for _ in range(n)]

        # All substrings of length 1 are
        # palindromes
        maxLength = 1
        i = 0
        while (i < n) :
            dp[i][i] = True
            i = i + 1

        # check for sub-string of length 2.
        i = 0
        while i < n - 1 :
            if (s[i] == s[i + 1]) :
                dp[i][i + 1] = True
                start = i
                maxLength = 2
                result = s[i:i+2]
            i = i + 1


        for j in range(n):
            for i in range(j):
                if (dp[i + 1][j - 1] and
                          s[i] == s[j]) :
                    dp[i][j] = True

                    if (len(s[i:j+1]) > maxLength) :
                        result = s[i:j+1]
                        maxLength = len(result)
        return result

    # Faster solution
     # def longestPalindrome(self, s: str) -> str:
    #     m = ''  # Memory to remember a palindrome
    #     for i in range(len(s)):  # i = start, O = n
    #         for j in range(len(s), i, -1):  # j = end, O = n^2
    #             if len(m) >= j-i:  # To reduce time
    #                 break
    #             elif s[i:j] == s[i:j][::-1]:
    #                 m = s[i:j]
    #                 break
        # return m