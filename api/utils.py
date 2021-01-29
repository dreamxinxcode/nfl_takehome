def format_date(date):
    date = date.split(' ')[0]
    date = date.split('-')
    date.reverse()
    return '-'.join(date)


def event_time(date):
    return date.split(' ')[1]


def get_team_rank(team, data):
    for item in data:
        if (item["team"] == team):
            return item["rank"]


def round_num(num):
    num = float(num)
    num = round(num)
    return '%.2f' % num


def get_rank_points(team, data):
    for item in data:
        if (item["team"] == team):
            return round_num(item["adjusted_points"])
