from datetime import datetime, date
from assignment_13_2 import today_string


today_date = datetime.strptime(today_string, "%A, %B %d, %Y,")

