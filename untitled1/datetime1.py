from datetime1 import datetime,timezone,timedelta

uct_dt = datetime.uctnow().replace(tzinfo=timezone.utc)
print(utc_dt)
