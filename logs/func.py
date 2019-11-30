import datetime


def utime_to_date(utime):
    #ミリ秒判定
    if len(str(utime)) > 11:
        utime = utime/1000

    date_utc = datetime.datetime.fromtimestamp(utime)
    date_jst = date_utc.astimezone(datetime.timezone(datetime.timedelta(hours=+9)))
    timestamp_jst = datetime.datetime.strftime(date_jst, '%Y-%m-%d %H:%M:%S')

    return timestamp_jst

if __name__ == '__main__':
    c = 1574096438800
    print(utime_to_date(c))
