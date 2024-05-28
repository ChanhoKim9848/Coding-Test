class Solution(object):
    def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):

        # Initialize the result variable to store the total number of training hours needed.
        res = 0

        # Iterate through each pair of energy and experience levels.
        for eg, exp in zip(energy, experience):
            
            # Check if the current energy level surpasses or equals the initial energy level.
            if eg >= initialEnergy:
                # If so, calculate the additional training hours needed to bridge the gap
                # between the initial and current energy levels, and add it to the result.
                res += eg - initialEnergy + 1
                # Update the initial energy level to reflect the new energy level.
                initialEnergy += eg - initialEnergy + 1

            # Check if the current experience level surpasses or equals the initial experience level.
            if exp >= initialExperience:
                # If so, calculate the additional training hours needed to bridge the gap
                # between the initial and current experience levels, and add it to the result.
                res += exp - initialExperience + 1
                # Update the initial experience level to reflect the new experience level.
                initialExperience += exp - initialExperience + 1

            # Update the initial energy and experience levels based on the current training session.
            initialEnergy -= eg
            initialExperience += exp
        
        # Return the total number of training hours needed to achieve desired levels.
        return res
