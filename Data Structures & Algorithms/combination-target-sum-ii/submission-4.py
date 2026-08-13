class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        total = []
        curr = []
        dupes = set()
        candidates.sort()
        def add(i):
            if sum(curr) == target and tuple(curr) not in dupes:
                total.append(curr.copy())
                dupes.add(tuple(curr))
            if sum(curr) > target or i == len(candidates):
                return
            curr.append(candidates[i])
            add(i+1)
            curr.pop()
            add(i+1)
        add(0)
        return total

                
        