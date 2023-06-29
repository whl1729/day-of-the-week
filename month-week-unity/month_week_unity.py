# Calculate the Month-Week-Unity days, which are both Monday and the first day of a month. 
import argparse
import calendar
from datetime import datetime

MONDAY = 0

def parse_args():
    parser = argparse.ArgumentParser(description="Calculate the Month-Week-Unity days")
    parser.add_argument("-s", "--start", type=int,
                        help="start year. The default is current year")
    parser.add_argument("-e", "--end", type=int,
                        help="end year (inclusive). The default is the same as start year")
    parser.add_argument("-q", "--quiet", action="store_true", default=False,
                        help="show only the number of Month-Week-Unity days in quiet mode")
    parser.add_argument("-n", "--num", type=int,
                        help="number of day. The end year will be ignored if num is provided")
    args = parser.parse_args()
    if not args.start:
        args.start = datetime.now().year
    if not args.end:
        args.end = args.start
    return args
    
def get_n_mwu_days(start, num):
    year = start
    count = 0
    mwu_days = []
    while count < num:
        for month in range(1, 13):
            if calendar.weekday(year, month, 1) == MONDAY:
                count += 1
                if count > num:
                    return mwu_days
                mwu_days.append(f"{year}-{month:02}-01")
        year += 1
    return mwu_days

def get_mwu_days_between(start, end):
    mwu_days = []
    for year in range(start, end+1):
        for month in range(1, 13):
            if calendar.weekday(year, month, 1) == MONDAY:
                mwu_days.append(f"{year}-{month:02}-01")
    return mwu_days

def get_mwu_days(args):
    if args.num:
        return get_n_mwu_days(args.start, args.num)
    
    return get_mwu_days_between(args.start, args.end)

def classify_mwu_days_by_year(mwu_days):
    mwu_days_by_year = {}
    for date in mwu_days:
        year = date.split('-')[0]
        if year in mwu_days_by_year:
            mwu_days_by_year[year].append(date)
        else:
            mwu_days_by_year[year] = [date]
    return mwu_days_by_year

def show_mwu_days(args, mwu_days):
    num = len(mwu_days)
    be, s = ['are', 's'] if num > 1 else ['is', '']
    if args.num:
        print(f'The {num} Month-Week-Unity day{s} since {args.start}-01-01 are as following.')
    else:
        print(f'There {be} {num} Month-Week-Unity day{s} between {args.start}-01-01 and {args.end}-12-31.')

    if args.quiet:
        return

    print('')
    mwu_days_by_year = classify_mwu_days_by_year(mwu_days)
    for mwu_days in mwu_days_by_year.values():
        print(' '.join(mwu_days))

def main():
    args = parse_args()
    mwu_days = get_mwu_days(args)
    show_mwu_days(args, mwu_days)

if __name__ == "__main__":
    main()