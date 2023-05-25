class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = {5:0,10:0,20:0}
        for bill in bills:
            if bill == 5:
                dic[5] += 1
            elif bill == 10:
                if dic[5]==0:
                    return False
                dic[5]-=1
                dic[10]+=1
            else:
                if dic[10]<1 and dic[5]<3:
                    return False
                if dic[10]>0 :
                    if dic[5]>0:
                        dic[10]-=1
                        dic[5]-=1
                        dic[20]+=1
                    else:
                        return False

                elif dic[5]>2:
                    dic[5]-=3
                    dic[20]+=1
        return True