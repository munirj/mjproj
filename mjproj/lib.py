def try_me():
    from datetime import datetime, date, timedelta

    today = datetime.now()
    tomorrow = datetime.now() + timedelta(days=1)
    midnight = datetime(year=tomorrow.year,
                        month=tomorrow.month,
                        day=tomorrow.day,
                        hour=0,
                        minute=0,
                        second=0)

    time_to_midnight = (midnight - today) / timedelta(minutes=1)
    print(f'It is {time_to_midnight:.0f} minutes to midnight')

try_me()
