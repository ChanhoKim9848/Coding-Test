class Solution(object):
    def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):
        ans = 0 
        for x, y in zip(energy, experience): 
            if initialEnergy <= x: 
                ans += x + 1 - initialEnergy
                initialEnergy = x + 1
            if initialExperience <= y: 
                ans += y + 1 - initialExperience
                initialExperience = y + 1
            initialEnergy -= x
            initialExperience += y 
        return ans 