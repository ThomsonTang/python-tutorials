import requests

if __name__ == '__main__':
    session = requests.Session()
    reponse = session.get('https://order.jd.com/center/list.action')
    print(session.cookies.get_dict())
