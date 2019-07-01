import requests

if __name__ == '__main__':
    resp_1 = requests.get('https://api.github.com/events')
    print(resp_1)
    # requests.post('', data={''})
