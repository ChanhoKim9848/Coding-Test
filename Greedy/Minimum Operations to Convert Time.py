class Solution(object):
    def convertTime(self, current, correct):
        a= (int(correct[:2])-int(current[:2]))*60+int(correct[3:5])-int(current[3:5])
        i=0
        res=0
        for i in [60,15,5,1]:
            res+=a//i
            a%=i
        return res



        