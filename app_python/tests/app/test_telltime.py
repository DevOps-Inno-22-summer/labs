import pytest


@pytest.mark.freeze_time('3rd Jan 2009', tz_offset=3)
def test_current_time(client, freezer):
    response = client.get("/api/v1/current_time")
    assert response.status_code == 200
    assert response.json() == {
        'time_zone': 'Europe/Moscow',
        'time': '2009-01-03T06:00:00+03:00',
    }

@pytest.mark.freeze_time('3rd Jan 2009', tz_offset=3)
def test_current_time_updates(client, freezer):
    response = client.get("/api/v1/current_time")
    assert response.status_code == 200
    assert response.json()['time'] == '2009-01-03T06:00:00+03:00'
    freezer.tick()
    response = client.get("/api/v1/current_time")
    assert response.status_code == 200
    assert response.json()['time'] == '2009-01-03T06:00:01+03:00'
