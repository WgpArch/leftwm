#!/usr/bin/env python3
import calendar
import datetime

def get_calendar():
    now = datetime.datetime.now()
    cal = calendar.TextCalendar(calendar.SUNDAY)
    
    # Header
    output = f"📅 {now.strftime('%B %Y')}\n\n"
    
    # Generate the month calendar
    month_cal = cal.formatmonth(now.year, now.month)
    output += month_cal
    
    # Add a little footer
    output += f"\nToday: {now.strftime('%A, %d %B %Y')}"
    
    return output

if __name__ == "__main__":
    print(get_calendar())
