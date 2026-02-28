import datetime

def parse_datetime(line):
    # Example: "2026-01-01 10:00:00 UTC+03:00"
    date_part, tz_part = line.split(" UTC")
    year, month, day = map(int, date_part.split()[0].split("-"))
    hour, minute, second = map(int, date_part.split()[1].split(":"))
    sign = 1 if tz_part[0] == "+" else -1
    tz_hours, tz_minutes = map(int, tz_part[1:].split(":"))
    offset = datetime.timedelta(hours=sign*tz_hours, minutes=sign*tz_minutes)
    local_time = datetime.datetime(year, month, day, hour, minute, second)
    utc_time = local_time - offset
    return utc_time

# Read input
start_line = input().strip()
end_line = input().strip()

start_utc = parse_datetime(start_line)
end_utc = parse_datetime(end_line)

duration = int((end_utc - start_utc).total_seconds())
print(duration)