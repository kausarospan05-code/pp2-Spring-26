import datetime

def parse_datetime(line):
    # Example: "2025-01-01 UTC+03:00"
    date_str, tz_str = line.split(" UTC")
    year, month, day = map(int, date_str.split("-"))
    sign = 1 if tz_str[0] == "+" else -1
    hours, minutes = map(int, tz_str[1:].split(":"))
    offset = datetime.timedelta(hours=sign*hours, minutes=sign*minutes)
    # Local midnight
    local_midnight = datetime.datetime(year, month, day, 0, 0, 0)
    # Convert to UTC
    utc_time = local_midnight - offset
    return utc_time

# Read input
line1 = input().strip()
line2 = input().strip()

t1 = parse_datetime(line1)
t2 = parse_datetime(line2)

diff_seconds = abs((t1 - t2).total_seconds())
days = int(diff_seconds // 86400)

print(days)