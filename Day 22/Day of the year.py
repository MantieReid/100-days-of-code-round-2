from datetime import datetime


class Solution:
  def dayOfYear(self, date: str) -> int:
    adate = datetime.strptime(date, "%Y-%m-%d")  # create a datetime object from the given string in this format.
    day_of_year = adate.timetuple().tm_yday  # get the current number day of the year
    return day_of_year
