from datetime import datetime
import pytz

import app


class Test:
    def test_current_time(self):
        moscow_timezone = pytz.timezone('Europe/Moscow')
        date_time = datetime.now(moscow_timezone)
        time = app.current_time()
        response_data_time = datetime.strptime(time[8:], '%Y:%m:%d %H:%M:%S %Z %z')
        assert (date_time - response_data_time).total_seconds() < 2
