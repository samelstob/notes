#!/usr/bin/env python

import sys, time, datetime

def datetime_from_time_tuple(time_tuple):
    """ Construct a datetime object from a time tuple.
    I'm sure there is an easier way to do this.
    I just can't work it out.
    """
    return datetime.datetime.fromtimestamp(time.mktime(time_tuple))


def parse_date(date_string):
    time_tuple = time.strptime(date_string, "%Y %b %d %H:%M:%S")
    return datetime_from_time_tuple(time_tuple)

for line in sys.stdin:
    fields = line.split()
    # Add the year (perhaps we should get this from the file timestamp)
    fields = [time.strftime("%Y")] + fields
    # Try turn the date into something sensible YYYY/MM/DD
    date_string = " ".join(fields[0:4])
    parsed_date = parse_date(date_string)
    fields = [str(parsed_date)] + fields[5:]
    print " ".join(fields)
