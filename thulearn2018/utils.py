import datetime

times_thresholds = [
        3*24*60*60, # red
        5*24*60*60, # yellow
        14*24*60*60, # blue
        30*24*60*60, # green
        ]

colors = [ "RED", "YELLOW", "BLUE", "GREEN" ]


def size_format(size_b):
    if size_b < 1024:
        return "%.2f" % (size_b)+'B'
    elif size_b < 1024*1024:
        return "%.2f" % (size_b/1024)+'KB'
    elif size_b < 1024*1024*1024:
        return "%.2f" % (size_b/1024/1024)+'MB'
    elif size_b > 1024*1024*1024*1024:
        return "%.2f" % (size_b/1024/1024/1024)+'GB'


def seconds_to_string(seconds):
    minute = 60
    hour = minute*60
    day = hour*24
    month = day*30
    result = ""
    t = [(month, "月"), (day, "天"), (hour, "小时"), (minute, "分钟")]
    for (s, c) in t:
        if seconds >= s:
            result += str((seconds//s))+c
            seconds %= s
    return result


def time_delta(t):
    sp = t.split(' ')
    tl = [int(x) for x in sp[0].split('-') + sp[1].split(':')]
    delta = datetime.datetime(tl[0], tl[1], tl[2], tl[3], tl[4], 0, 0) - \
        (datetime.datetime.utcnow() + datetime.timedelta(hours=8))
    delta_seconds = delta.days*24*60*60+delta.seconds
    for i in range(len(times_thresholds)):
        if delta_seconds < times_thresholds[i]:
            return (seconds_to_string(delta_seconds), colors[i])
    return (seconds_to_string(delta_seconds), "GREEN")


def expired(timeStr):
    return timeStr < datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
