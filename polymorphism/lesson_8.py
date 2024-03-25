API_URL = 'http://localhost:8080/api/v2/'


class WeatherService():
    # BEGIN (write your solution here)
    def __init__(self, client):
        self.client = client

    def look_up(self, city):
        return requests_client(city, self.client)


def requests_client(city, lib):
    request = f"{API_URL}cities/{city}"
    raw_response = lib.get(request)
    response = raw_response.json()
    return response
# END
