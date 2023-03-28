"""
related time file
"""
import datetime
import calendar
from datetime import date, datetime as dt
import pandas as pd


class Date:

    def today_(self, n):
        from datetime import datetime, timedelta
        today = datetime.now()
        today = today + timedelta(days=n)
        today = datetime.strftime(today, "%Y-%m-%d")
        today = pd.to_datetime(today).date()
        return today

    def start_day(self, n):
        today = self.today_(n)
        start_day = datetime.datetime(today.year, today.month, 1)
        start_day = datetime.datetime.strftime(start_day, "%Y-%m-%d")
        start_day = datetime.datetime.strptime(start_day, "%Y-%m-%d")
        start_day = pd.to_datetime(start_day).date()
        return start_day

    def last_day(self, n):
        begin_day = self.start_day(n)
        month_end_day = calendar.monthrange(begin_day.year, begin_day.month)[1]
        last_day = datetime.datetime(begin_day.year, begin_day.month, month_end_day)
        return last_day

    def current_time(self) -> datetime:
        current_time = dt.strftime(dt.now(), '%Y-%m-%d %H:%M:%S')
        return current_time
