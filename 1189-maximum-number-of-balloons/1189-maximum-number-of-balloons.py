class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ballon_map = {'b':1, 'a':1, 'l':2, 'o':2, 'n':1}
        max_instances = 0
        text_map = {}

        for char in text:
            if char in ballon_map:
                if char in text_map:
                    text_map[char] += 1
                else:
                    text_map[char] = 1

        min_count = float('inf') 

        for char in ballon_map:
            if char in text_map:
                count = text_map[char] // ballon_map[char]
                min_count = min(min_count, count)
            else:
                return 0 
        return min_count
            

