from datetime import datetime
from dateutil.relativedelta import relativedelta


current_date = datetime.now().strftime("%d %b, %a")
next_date = (datetime.now() + relativedelta(day=2)).strftime("%d %b, %a")
print(current_date)
print(next_date)
