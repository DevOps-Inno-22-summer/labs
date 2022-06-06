from datetime import datetime

import app


class TestApp:

    def test_time_generation(self):
        time = app.generate_moscow_time()
        assert ":" in time

    def test_http_response(self):
        response = app.index()
        assert "Moscow time is" in response

    def test_time_formatting(self):
        assert app.format_time(datetime(2022, 6, 6, 23, 55, 3)) == "23:55:03"
        assert app.format_time(datetime(2022, 6, 6, 1, 1, 0)) == "01:01:00"
        assert app.format_time(datetime(2022, 6, 6, 13, 0, 22)) == "13:00:22"
