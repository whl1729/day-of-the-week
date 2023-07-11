# Calculate the day of the week with the Doomsday rule.
import argparse

# The date of the doomsday occurs at each month of a common year.
# That is: 1/3, 2/28, 3/0, 4/4, 5/9, 6/6, 7/11, 8/8, 9/5, 10/10, 11/7, 12/12
common_year_doomsday = [3, 28, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]

# The date of the doomsday occurs at each month of a leap year.
# That is: 1/4, 2/29, 3/0, 4/4, 5/9, 6/6, 7/11, 8/8, 9/5, 10/10, 11/7, 12/12
leap_year_doomsday = [4, 29, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]

week_day_names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def parse_args():
    parser = argparse.ArgumentParser(description="Calculate the day of the week for the given date")
    parser.add_argument("date", help="format: yyyy-mm-dd")
    args = parser.parse_args()
    return args

def get_day_of_the_week(date):
    year, month, day = [int(d) for d in date.split('-')]
    century_anchor = 5 * ((year // 100) % 4) % 7 + 2
    year_anchor = (year % 100) // 4 + (year % 100)
    doomsday = (century_anchor + year_anchor) % 7
    # If it is a leap year
    if year % 400 == 0 or ((year % 100 > 0) and (year % 4 == 0)):
        distance = day - leap_year_doomsday[month-1]
    else: # it is a common year
        distance = day - common_year_doomsday[month-1]
    
    index = (doomsday + distance) % 7
    return week_day_names[index]

def main():
    args = parse_args()
    day = get_day_of_the_week(args.date)
    print(f"{args.date} is {day}.")

if __name__ == "__main__":
    main()