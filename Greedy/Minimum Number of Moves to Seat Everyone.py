class Solution(object):
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        return sum(abs(e-t) for e,t in zip(seats, students))

print(Solution.minMovesToSeat(Solution,[3,1,5],[2,7,4]))