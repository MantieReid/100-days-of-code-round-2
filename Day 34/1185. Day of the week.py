from datetime import datetime

class Solution:
  def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
    date = datetime(year=year,day=day, month=month) # convert the number date into a datetime object
    return date.strftime('%A') # get the day of the week from date and return it.




