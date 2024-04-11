class Solution(object):
    def canThreePartsEqualSum(self, arr):
        avg,remainder,part,c=sum(arr)//3,sum(arr)%3,0,0
          # 22 / 3
        for i in arr:
            part+=i
            if part==avg:
                part=0
                c+=1
        if c>=3 and remainder==0:
            return True
        return False
            





        

        


        



