class Solution:
    def isHappy(self, n: int) -> bool:
        current_number = n
        seen_numbers = set()

        while True:
            new_number = 0
            for digit in str(current_number):
                new_number += int(digit) ** 2

            if new_number in seen_numbers:
                return False
            if new_number == 1:
                return True
            
            seen_numbers.add(new_number)
            current_number = new_number
