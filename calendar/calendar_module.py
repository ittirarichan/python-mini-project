# calendar_module.py

import calendar

def display_calendar(year, month):
    """
    Function to display a calendar for a given year and month.
    """
    cal = calendar.monthcalendar(year, month)

    # Displaying the calendar header
    month_name = calendar.month_name[month]
    print(f"{'=' * 20} {month_name} {year} {'=' * 20}")
    print("Mon Tue Wed Thu Fri Sat Sun")

    # Displaying the calendar rows
    for week in cal:
        week_str = ""
        for day in week:
            if day == 0:
                week_str += "   "  # Display blank space for days not in this month
            else:
                week_str += f"{day:2} "  # Display the day with padding
        print(week_str)

    print("=" * 52)  # Separator line after the calendar
