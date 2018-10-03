    

## 第一題
def reverseNumber(s):
    ans=""
    s = s.split(' ')
    for i in s:
        ans += i[::-1]
        ans+= " "
    return ans
    
    

##第二題
def B(x):
    x += 1
    ans = []
    for i in range(x):
        if i % 3 == 0 and i % 5 ==0:
            i = str(i)
            ans.append(i)
            
        elif i % 5 == 0 or i % 3 ==0:
            continue
        else:
            
            i = str(i)
            ans.append(i)
    return len(ans)
    
        

        