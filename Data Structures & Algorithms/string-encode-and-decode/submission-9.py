class Solution:

    delimiter = '|'

    def encode(self, strs: List[str]) -> str:
        # "15|fdgwgw12|dffdfdf4|vfdfsddf"
        string = []

        for _str in strs:
            str_length = len(_str)
            string.append("".join([str(str_length), self.delimiter, _str]))

        return "".join(string)


    def decode(self, s: str) -> List[str]:
        ret = []
        str_length = len(s)
        read_index = 0
        while True:
            if read_index >= str_length:
                break
            
            delimiter_position = s.find(self.delimiter, read_index)
            next_str_length = int(s[read_index : delimiter_position])
            read_index = delimiter_position + 1
            if next_str_length == 0:
                ret.append("")
            else:
                ret.append(s[read_index : read_index + next_str_length])
                read_index = read_index + next_str_length

        return ret
