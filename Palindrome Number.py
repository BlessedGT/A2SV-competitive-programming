class Solution:
    def isPalindrome(self, x: int) -> bool:
        frst = str(x)
        if frst == frst[::-1]:
            return True
        else:
            return False
