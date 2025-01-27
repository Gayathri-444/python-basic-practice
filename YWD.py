N = int(input())

year = N//365
week = ((N%365)//7)
rem_days = ((N%365)%7)

print("years: ",year)
print("weeks: ",week)
print("days: ",rem_days)
