class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l, r = 0, len(skill)-1
        sm = 0
        ch = (skill[l] + skill[r])
        
        while (l < r):
            if skill[l] + skill[r] == ch:
                sm += (skill[l] * skill[r])
                l += 1
                r -= 1
            else:
                return -1
        return sm
