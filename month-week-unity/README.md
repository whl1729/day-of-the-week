# Month Week Unity

Calculate the days that are both Monday and the first day of a month. 

For simplicity sake, let's refer to these days as **Month-Week-Unity days**.
So why do we care about Month-Week-Unity days?

Because they're both **interesting** and **useful**.

On the one hand, there are many interesting statements hidden behind them:

1. There are 1 to 3 Month-Week-Unity days every year.

On the other hand, once you know a Month-Week-Unity day, it's easy for you to know what day of the week other days in the same month are. All you need to do is calculating its remainder when divided by 7.

For example, 2023-05-01 is Monday, so 2023-05-08 is also Monday because `8 % 7 = 1`, and 2023-05-23 is Tuesday because `23 % 7 = 2`.

## Getting Started

### Requirements

- Python 3

## Usage

- Find Month-Week-Unity days in current year:

```sh
$ python3 month_week_unity.py 
There is 1 Month-Week-Unity day between 2023-01-01 and 2023-12-31.

2023-05-01
```

- Find Month-Week-Unity days between 2046 and 2050:

```sh
$ python3 month_week_unity.py -s 2046 -e 2050
There are 9 Month-Week-Unity days between 2046-01-01 and 2050-12-31.

2046-01-01 2046-10-01
2047-04-01 2047-07-01
2048-06-01
2049-02-01 2049-03-01 2049-11-01
2050-08-01
```

- Find 10 Month-Week-Unity days since 2100:

```sh
$ python3 month_week_unity.py -s 2100 -n 10
The 10 Month-Week-Unity days since 2100-01-01 are as following.

2100-02-01 2100-03-01 2100-11-01
2101-08-01
2102-05-01
2103-01-01 2103-10-01
2104-09-01 2104-12-01
2105-06-01
```

- Find how many Month-Week-Unity days between 2000 and 3000:

```sh
$ python3 month_week_unity.py -s 2000 -e 3000 -q
There are 1711 Month-Week-Unity days between 2000-01-01 and 3000-12-31.
```

- Get the help information:

```sh
$ python3 month_week_unity.py -h
usage: month_week_unity.py [-h] [-s START] [-e END] [-q] [-n NUM]

Calculate the Month-Week-Unity days

optional arguments:
  -h, --help            show this help message and exit
  -s START, --start START
                        start year. The default is current year
  -e END, --end END     end year (inclusive). The default is the same as start year
  -q, --quiet           show only the number of Month-Week-Unity days in quiet mode
  -n NUM, --num NUM     number of day. The end year will be ignored if num is provided
```
