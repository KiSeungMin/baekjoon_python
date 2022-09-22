hourNow, minuteNow = map(int, input().split(" "))
addMinute = int(input())
minuteNow = minuteNow + addMinute

if (minuteNow >= 60):
    addHour = minuteNow // 60
    minuteNow = minuteNow % 60
    hourNow = hourNow + addHour
    
if(hourNow >= 24):
    hourNow = hourNow % 24
    
print(f'{hourNow} {minuteNow}')