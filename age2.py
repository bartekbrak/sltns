"""
A very advanced tool to calculate various dates.
"""

import argparse
import sys
import datetime


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '--date-in-days',
        type=int,
        help='print out the date in that many days from now'
    )
    parser.add_argument(
        '--date-since',
        action='store_true',
        help='print the time in days since that date'
    )
    parser.add_argument(
        '-y',
        '--year',
        type=int
    )
    parser.add_argument(
        '-m',
        '--month',
        type=int
    )
    parser.add_argument(
        '-d',
        '--day',
        type=int
    )
    args = parser.parse_args()
    if args.date_in_days and args.date_since:
        print 'You cannot use date-in-days and date-since together.'
        parser.print_usage()
        sys.exit(1)
    if not args.date_in_days and not args.date_since:
        parser.print_usage()
        sys.exit(128)
    if args.date_since and not all([args.year, args.month, args.day]):
        parser.print_usage()
        print '--date-since requires also --year --month and --day.'
        sys.exit(128)
    return args


def main():
    args = parse_args()
    if args.date_in_days:
        print 'date in {} days {}'.format(
            args.date_in_day, 
            days_from_now(date_in_days)
        ) 
    elif args.date_since:
        delta = days_since(args.year, args.month, args.day)
        print 'days since then: {delta.days}'.format(delta=delta)


def days_from_now(days):
    return (datetime.datetime.now() + datetime.timedelta(days=int(days)))


def days_since(year, month, day):
    then = datetime.datetime(year, month, day)
    now = datetime.datetime.now()
    return now - then


if __name__ == '__main__':
    main()
