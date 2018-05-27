from datetime import datetime,timezone,timedelta
import re

def to_timestamp(dt_str,tz_str):
    p2 = re.match("UTC([+|-]\d{1,2}):\d{2}", tz_str)
    i = int(p2.group(1))
    cday = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    dt = cday.astimezone(timezone(timedelta(hours=i)))
    print(dt.timestamp())


t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')


t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')


print('ok')