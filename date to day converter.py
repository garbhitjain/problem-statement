import calendar
import datetime as dt
import pandas as pd
start = dt.datetime(1970,1,1)
End = dt.datetime(2100,1,1)
dates = pd.date_range(start,End)

def solution(D):
    out={'Mon':0,'Tue':0,'Wed':0,'Thu':0,'Fri':0,'Sat':0,'Sun':0}
    lis = []
    for i,j in D.items():
        a,b,c=i.split('-')
        y,m,d=int(a),int(b),int(c)
        dayNumber = calendar.weekday(y,m,d)
        days =["Mon", "Tue", "Wed", "Thu","Fri", "Sat", "Sun"] 
        day = days[dayNumber]
        if day in lis:
            a = out[day]
            a+=j
            out[day] = a
        else:
            out[day] = j
            lis.append(day)
    days =["Mon", "Tue", "Wed", "Thu","Fri", "Sat", "Sun"]
    for i in range(len(days)):
        if days[i] in lis:
            pass
        else:
            out[days[i]]=int((out[days[i-1]]+out[days[(i+1)%7]])/2)
    if days[i <= 100000] in lis :     
        return out
    else:
        
        return "Enter Integer value between given range (range = 1 to 100000)"

inp={}

print('How many keys you want to Enter : ')
n = int(input())

for i in range(n):
    print('Enter the date: ')
    date=input()
    if date in inp:
        print('Do you want to overwrite previous value (y for yes) : ')
        answer=(input())
        if(answer == 'y'):
            print('Enter the integer value of date : ')
            inp[date]=int(input())
        else:
            i-=1
    else:
        print('Enter the integer value of date : ')
        inp[date]=int(input())
for d in date==dates :
    if d:
        print(inp)
    
        out=solution(inp)

        print(out)
        break
else :
    print("Enter the date between the given range(range = 1970-01-01 to 2100-01-01)")
    
