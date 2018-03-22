import datetime

from processbar.process_bar import draw
import time


def get_percent():
    now = time.localtime(time.time())
    passed_days = now.tm_yday
    year = now.tm_year
    start_date = datetime.datetime(year=year, month=1, day=1)
    end_date = datetime.datetime(year=year, month=12, day=31)
    total_days = (end_date - start_date).days + 1
    percentage = int(round((float(passed_days) / float(total_days)) * 100, 0))

    return passed_days, percentage


if __name__ == '__main__':
    passed, percent = get_percent()
    print("Passed %s days:" % passed)
    draw(percent)
