import app


def test_time_generation():
    time = app.generate_moscow_time()
    assert ":" in time


def test_http_response():
    response = app.index()
    assert "Moscow time is" in response


if __name__ == "__main__":
    test_time_generation()
    test_http_response()
    print("Tests passed")
