class Solution:

    def encode(self, strs: List[str]) -> str:
        to_assemble = []
        for _str in strs:
            to_assemble.append(f"{len(_str)}:{_str}")
        ret = "".join(to_assemble)
        return ret

    def decode(self, s: str) -> List[str]:
        ret = []
        left_ptr = 0
        while left_ptr < len(s):
            right_ptr = left_ptr
            while s[right_ptr] != ':':
                right_ptr += 1
            piece_length = int(s[left_ptr : right_ptr])
            left_ptr = right_ptr + 1
            ret.append(s[left_ptr : left_ptr + piece_length])
            left_ptr += piece_length

        return ret