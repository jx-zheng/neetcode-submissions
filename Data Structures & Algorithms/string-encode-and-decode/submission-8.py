class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for _str in strs:
            str_length = len(_str)
            encoded.append(f'{str_length}.{_str}')

        return ''.join(encoded)


    def decode(self, s: str) -> List[str]:
        decoded = []

        index = 0
        while index < len(s):
            # get segment length
            delimiter_location = s.find('.', index)
            segment_length = int(s[index:delimiter_location])
            index = delimiter_location + 1
            # build segment
            segment_end = index + segment_length
            decoded.append(s[index:segment_end])
            index = segment_end

        return decoded
