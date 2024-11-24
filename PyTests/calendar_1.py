import calendar

def print_calendar(year, month):
    cal = calendar.month(year, month)
    print(cal)

def main():
    year = 2023
    for month in range(1, 13):
        print()
        print(f"Calendar for {calendar.month_name[month]} {year}:")
        print()
        print_calendar(year, month)
        print()

if __name__ == "__main__":
    main()
