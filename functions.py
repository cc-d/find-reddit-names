def parse_headers(filename):
    with open(filename,'r') as f:
        headers = f.read().splitlines()
        headers = [x.split(':') for x in headers]
        hd = {}
        for h in headers:
            if h[0]:
                if len(h) > 2:
                    h[1] = ':'.join(h[1:])
                hd[h[0]] = h[1]
        return hd

def check(name):
    import requests
    import json
    headers = parse_headers('headers.txt')
    r = requests.post('https://www.reddit.com/api/check_username.json', data={'user':name}, headers=headers)
    j = json.loads(r.text)
    if j == {}:
        return True
    else:
        return False
