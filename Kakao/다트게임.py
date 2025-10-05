def solution(dartResult):
    # 1D2S#10S
    
    option_dict = {'S':1,'D':2,'T':3}
    bonus = '#*'
    scores=[]
    i=0
    n=len(dartResult)
    
    while i < n : 
        score = 0
        if dartResult[i] == '1' and i+1 < n and dartResult[i+1]=='0':
            score = 10
            i+=2
        else:
            score=int(dartResult[i])
            i+=1
        
        if dartResult[i] in option_dict:
            score **= option_dict[dartResult[i]]
            i+=1
        
        if i<n and dartResult[i] in bonus:
            if dartResult[i]=='*':
                score*=2
                if scores:
                    scores[-1]*=2
            elif dartResult[i]=='#':
                score*=-1
            i+=1 
        scores.append(score)
    return sum(scores)
    
    
    