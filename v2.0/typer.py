import pyautogui
import pyperclip
from OAuth import *  # Import necessary libraries and OAuth module for authorization

# Define dictionaries for months and days of the week
months = {'Jan': 1, 'Feb': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'Aug': 8, 'Sept': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
DaysInWeek = {'Sun': 0, 'Mon': 1, 'Tues': 2, 'Wed': 3, 'Thurs': 4, 'Fri': 5, 'Sat': 6}

# Get calendar events using OAuth authentication
event = get_events("primary")

# Function to add leading zero to single-digit numbers
def AddZero(day):
    return f"0{day}" if len(str(day)) == 1 else str(day)

# Function to format dates as "YYYY-MM-DD"
def GetFormattedDate(year, month, day):
    return f"{year}-{AddZero(month)}-{AddZero(day)}"

# Function to get the day of the week name based on its value
def get_day_name(val):
    return next((key for key, value in DaysInWeek.items() if value == val), "key doesn't exist")

# Function to check if a year is a leap year
def IsLeapYear(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

# Function to calculate the day of the week for the first day of a month
def FirstDayOfMonth(year, month):
    weekday = DaysInWeek['Mon']
    # Calculate day of the week for the first day of each year leading up to the given year
    for i in range(1900, year):
        weekday = (weekday + 365) % 7
        if IsLeapYear(i):
            weekday = (weekday + 1) % 7
    # Calculate day of the week for the first day of the given month
    for i in range(1, month):
        weekday = (weekday + MonthDays(year, i)) % 7
    return get_day_name(weekday)

# Function to get the number of days in a month
def MonthDays(year, month):
    if month == 2:
        return 29 if IsLeapYear(year) else 28
    return 30 if month in [4, 6, 9, 11] else 31

# Function to write contents on a OneNote page
def WriteOnPage(contents):
    pyautogui.press(['down', 'down'])
    for content in contents:
        pyautogui.hotkey('ctrl', '1')
        pyperclip.copy(content)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('down')

# Function to create a new month section in OneNote
def CreateMonth(month):
    pyautogui.hotkey('ctrl', 't')
    pyperclip.copy(month)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('Enter')

# Function to create dates and associated events in a month section
def CreateDates(FirstDay, DaysInMonths, year, month):
    dates = [str(i) for i in range(1, DaysInMonths + 1)]
    default = DaysInWeek[FirstDay]
    for date in dates:
        suffix = 'st' if date[-1] == '1' else 'nd' if date[-1] == '2' else 'rd' if date[-1] == '3' else 'th'
        pyperclip.copy(f"{date}{suffix}")
        pyautogui.hotkey('ctrl', 'v')
        AddDays(default)
        default = (default + 1) % 7
        try:
            WriteOnPage(event[GetFormattedDate(year, month, date)])
        except KeyError:
            pass
        pyautogui.hotkey('ctrl', 'n')

# Function to add day of the week to the end of a date entry
def AddDays(default):
    pyperclip.copy(f" ({get_day_name(default)})")
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('Enter')

# Function to create the schedule for a given year
def CreateSchedule(year):
    for month in months:
        FirstDay = FirstDayOfMonth(year, months[month])
        DaysInMonths = MonthDays(year, months[month])
        CreateMonth(month)
        CreateDates(FirstDay, DaysInMonths, year, months[month])
