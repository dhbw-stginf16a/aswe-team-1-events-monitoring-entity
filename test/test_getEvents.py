import pytest

from .TestConnexion import TestConnexion


@pytest.mark.usefixtures('client')
class TestRequest(TestConnexion):
    """A test to get events from the monitoring api
    """

    def test_getEvents(self, client):
        request = {
            "payload": {
                "categories": ["concerts", "performing-arts"],
                        "location": "@48.7744476,9.1714984,17.5",
                        "start_date": "2019-03-29",
                        "end_date": "2019-04-30"
            },
            "type": "current_events"
        }

        response = client.post('api/v1/request', json=request)

        assert response.status_code == 200
        print(response.get_json())
