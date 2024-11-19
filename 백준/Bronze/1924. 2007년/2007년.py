import sys
input = sys.stdin.readline


N,M = map(int,input().strip().split())

month = [31,28,31,30,31,30,31,31,30,31,30,31]

week = ['SUN','MON','TUE','WED','THU','FRI','SAT']

total_day = sum(month[:N-1]) + M

day_week = (total_day) % 7

print(week[day_week])