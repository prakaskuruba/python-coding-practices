# To display todays date
import datetime
today = datetime.date.today()
print(today)
#To display the date next one week from the current date.
today = datetime.date.today()
one_week_form_date=today+datetime.timedelta(days=7)
print(one_week_form_date)
#To display  the date before one week from the current date.
today = datetime.date.today()
last_week_form_date = today - datetime.timedelta(days=7)
print(last_week_form_date)