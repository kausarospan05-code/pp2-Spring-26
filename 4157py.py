import datetime
import calendar

def parse_datetime(line):
    # Example: "2000-05-10 UTC+03:00"
    date_str, tz_str = line.split(" UTC")
    year, month, day = map(int, date_str.split("-"))
    sign = 1 if tz_str[0] == "+" else -1
    hours, minutes = map(int, tz_str[1:].split(":"))
    offset = datetime.timedelta(hours=sign*hours, minutes=sign*minutes)
    local_midnight = datetime.datetime(year, month, day, 0, 0, 0)
    utc_time = local_midnight - offset
    return (year, month, day, utc_time)

# Read input
birth_line = input().strip()
current_line = input().strip()

by, bm, bd, _ = parse_datetime(birth_line)
cy, cm, cd, current_utc = parse_datetime(current_line)

# Handle Feb 29 birthdays
def birthday_for_year(year, month, day):
    if month == 2 and day == 29 and not calendar.isleap(year):
        return datetime.date(year, 2, 28)
    return datetime.date(year, month, day)

# Find next birthday (not earlier than current date)
candidate_year = cy
bday_date = birthday_for_year(candidate_year, bm, bd)
bday_local = datetime.datetime(candidate_year, bday_date.month, bday_date.day, 0, 0, 0)

# Parse again to get UTC for birthday (same timezone as birth_line)
_, _, _, birth_utc0 = parse_datetime(birth_line)  # just to get offset
# Extract offset from birth_line
tz_str = birth_line.split(" UTC")[1]
sign = 1 if tz_str[0] == "+" else -1
hours, minutes = map(int, tz_str[1:].split(":"))
offset = datetime.timedelta(hours=sign*hours, minutes=sign*minutes)
bday_utc = bday_local - offset

if bday_utc < current_utc:
    candidate_year += 1
    bday_date = birthday_for_year(candidate_year, bm, bd)
    bday_local = datetime.datetime(candidate_year, bday_date.month, bday_date.day, 0, 0, 0)
    bday_utc = bday_local - offset

diff_seconds = (bday_utc - current_utc).total_seconds()
if diff_seconds == 0:
    print(0)
else:
    days = int((diff_seconds + 86399) // 86400)  # ceil
    print(days)