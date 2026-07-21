class Solution:

  def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
    # Zip pairs (height, name) together, sort by height descending, then extract names
    people = sorted(zip(heights, names), reverse=True)
    return [name for height, name in people]