class Solution:
    def isPalindrome(self, s: str) -> bool:
        l_ptr = 0
        r_ptr = len(s) - 1
        while True:
            if l_ptr >= r_ptr:
                return True
            while not s[l_ptr].lower().isalnum():
                print(l_ptr)
                if l_ptr == len(s) - 1:
                    return True
                l_ptr += 1
            while not s[r_ptr].lower().isalnum():
                if r_ptr == 0:
                    return True
                r_ptr -= 1
            if not s[l_ptr].lower() == s[r_ptr].lower():
                print(f"{l_ptr} | {r_ptr}")
                return False
            l_ptr += 1
            r_ptr -= 1

            # racecar
            # Was it a car or a cat I saw?

