


def r(s, start,end,elist):
    
    if start >= end:
        temp=0
        for i in range(len(s)-1):
            temp=temp+abs(s[i+1][0]-s[i][0])+abs(s[i+1][1]-s[i][1])
            
           
        elist.append(temp)
        
        
    else:
        for i in range(start,end):
            s[start],s[i] = s[i],s[start]
            r(s, start+1, end,elist)
            s[start], s[i] = s[i], s[start]
            
s=[(5,2),(4,2),(1,4),(4,5)]
 


def perm(s):
    start = 0
    end = len(s)
    elist=[]
    r(s, start,end,elist)
    smallist=[]
    num=int(len(elist)/end)
    
    while start<=len(elist)-num:
        small=min(elist[start:start+num])
        
        smallist.append(small)
        start+=num
    print(smallist)

perm(s)
