class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        right_ptr = len(digits) - 1
        while right_ptr >= 0:
            if digits[right_ptr] != 9:
                digits[right_ptr] += 1
                return digits
            digits[right_ptr] = 0
            right_ptr -= 1

        one = [1]
        one.extend(digits)
        return one
        