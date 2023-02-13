import calendar
import datetime

y = datetime.date.today().year
m = datetime.date.today().month

print(calendar.calendar(y, m))