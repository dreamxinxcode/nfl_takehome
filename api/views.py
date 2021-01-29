from .utils import format_date, event_time, get_team_rank, get_rank_points, round_num
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests


@api_view(['GET'])
def events_view(request, to_date, from_date):
    events_url = f'https://delivery.chalk247.com/scoreboard/NFL/{from_date}/{to_date}.json?api_key=74db8efa2a6db279393b433d97c2bc843f8e32b0'
    team_rankings_url = 'https://delivery.chalk247.com/team_rankings/NFL.json?api_key=74db8efa2a6db279393b433d97c2bc843f8e32b0'

    # Parsed data
    events = requests.get(events_url).json()
    team_rankings = requests.get(team_rankings_url).json()
    events_list = events['results']

    res = []

    for date in events_list:
        current_date = events_list[date]

        # Check if current_date isn't empty
        if current_date:
            for id in current_date['data']:
                event = current_date['data'][id]
                away_city = event['away_city'],
                home_city = event['home_city'],
                rankings = team_rankings['results']['data']

                obj = {
                    'event_id': event['event_id'],
                    'event_date': format_date(event['event_date']),
                    'event_time': event_time(event['event_date']),
                    'away_team_id': event['away_team_id'],
                    'away_nick_name': event['away_nick_name'],
                    'away_city': away_city[0],
                    'away_rank': get_team_rank(away_city[0], rankings),
                    'away_rank_points': get_rank_points(away_city[0], rankings),
                    'home_team_id': event['home_team_id'],
                    'home_nick_name': event['home_nick_name'],
                    'home_city': home_city[0],
                    'home_rank': get_team_rank(home_city[0], rankings),
                    'home_rank_points': get_rank_points(home_city[0], rankings)
                }

                res.append(obj)

    return Response(res)
