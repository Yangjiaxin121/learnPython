

from enum import Enum,unique

Month = Enum('Month',('Jan','Feb','Mar','Apr','May',
                      'Jun','Jul','Aug','Sep','Oct','Nov','Dec'))

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)

day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(day1 == Weekday.Mon)
print(day1 == Weekday.Tue)
print(Weekday(1))
print(day1 == Weekday(1))
for name,member in Weekday.__members__.items():
    print(name,'=>',member)