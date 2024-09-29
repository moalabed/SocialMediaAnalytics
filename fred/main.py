import requests

api_key = '530aa1f8b29b07bf2c0901001ebe7624'

def construct_url(endpoint, series_id, realtime_start, realtime_end, api_key, filetype):
    base_url = 'https://api.stlouisfed.org'
    return f"{base_url}/{endpoint}?series_id={series_id}&realtime_start={realtime_start}&&realtime_end={realtime_end}&api_key={api_key}&file_type={filetype}"

def send_get_request(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"{response.status_code} and text is {response.text}")

if __name__ == "__main__":
    endpoint = 'fred/series/observations'
    series_id = 'DEXUSEU'
    realtime_start = '2000-01-01'
    realtime_end = '2024-09-22'
    filetype ='json'
    url = construct_url(endpoint, series_id, realtime_start, realtime_end, api_key, filetype)
    response = send_get_request(url)
    print(url)
    print(response)