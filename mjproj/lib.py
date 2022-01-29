def try_me():
    from datetime import date
    from datetime import datetime, timedelta

    now = datetime.now()
    demo_time = datetime.min.time()
    demo_date = date(2022, 3, 19)
    demo_day = datetime.combine(demo_date, demo_time) + timedelta(hours=10)

    days = (demo_day - now) / timedelta(days=1)
    hours = ((demo_day - now) % timedelta(days=1)) / timedelta(hours=1)
    mins = ((demo_day - now) % timedelta(hours=1)) / timedelta(minutes=1)
    secs = ((demo_day - now) % timedelta(minutes=1)) / timedelta(seconds=1)

    print(
        f'It is {days:.0f} days, {hours:.0f} hours, {mins:.0f} minutes and {secs:.0f} seconds to demo day...'
    )

try_me()
