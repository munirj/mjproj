def try_me():
    from datetime import date
    from datetime import datetime, timedelta

    now = datetime.now()
    demo_time = datetime.min.time()
    demo_date = date(2022, 3, 19)
    demo_day = datetime.combine(demo_date, demo_time) + timedelta(hours=10)

    days_to_demo = (demo_day - now) / timedelta(days=1)

    print(f'It is {days_to_demo:.0f} days to demo day')

try_me()
