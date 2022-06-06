from datetime import datetime
import pytz

import app


class Test:
    def test_current_time(self):
        moscow_timezone = pytz.timezone('Europe/Moscow')
        date_time = datetime.now(moscow_timezone)
        time = app.current_time()
        date_time_str = date_time.strftime('%Y:%m:%d %H:%M:%S %Z %z')
        assert date_time_str == time[8:]
