import datetime
from calendar import monthrange

from processbar.process_bar import draw


def get_percent():
    now = datetime.datetime.now()
    days = monthrange(now.year, now.month)[1]
    today = now.day
    percentage = int(round((float(today) / float(days)) * 100, 0))
    return today, days, percentage

if __name__ == '__main__':
    cur_day, total, percent = get_percent()
    print("Month percentage %(elapsed)s / %(total)s" % {'elapsed': cur_day, 'total': total})
    draw(percent)
