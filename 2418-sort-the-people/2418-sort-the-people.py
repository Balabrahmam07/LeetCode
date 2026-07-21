class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l = []
        for _ in names:
            l.append(names[heights.index(max(heights))])
            max_idx = heights.index((max(heights)))
            heights[max_idx] = 0
        return l