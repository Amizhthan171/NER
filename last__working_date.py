from datetime import date, timedelta

today = date.today()
weekday = today.weekday()

if weekday == 0:
    last_working_day = today - timedelta(days=3)
else:
    last_working_day = today - timedelta(days=1)

formatted_date = last_working_day.strftime("%m/%d/%Y")
print("Last working day:", formatted_date)
