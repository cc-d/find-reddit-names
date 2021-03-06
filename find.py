import requests
from random import shuffle
from time import sleep
from itertools import product
from functions import parse_headers, check

def main():
    name_length = 3 # length of names to brute force
    delay = 2 # time between requests
    user_agent = 'Just looking for some unique usernames 1.0'
    chars = 'abcdefghijklmnopqrstuvwxyz123456789-_'# 
    names = []

    for x in product(chars, repeat=3):
        j = ''.join(x)
        names.append(''.join(x))

    shuffle(names) # inceases chances of finding aname
    mnames = len(names)
    count = 0
    print mnames, 'possible names.'
    print 'It will take', ((mnames * delay)/60)/60, 'hours to finish at minimum. Sit back, grab some coffee, screen and forget.'

    for name in names:
        headers = {'User-Agent': user_agent}
        r = requests.get('https://www.reddit.com/user/%s' % name, headers=headers)
        
        zsleep = 2
        while r.status_code == 403: # if forbidden retry in 1 second
            r = requests.get('https://www.reddit.com/user/%s' % name, headers=headers)
            print 'Sleeping for', zsleep
            sleep(zsleep)
            zsleep = zsleep + zsleep
            if zsleep >= 32: # limit maximum number of retires
                break

        if r.status_code == 404:
            sleep(2)
            result = check(name)
            if result:
                with open('possible.txt', 'a+') as p:
                    p.write(name + '\n')
                print 'Possible Name!:', name
            else:
                print 'Name returned 404 but failed availibility check:', name
        count += 1
        print count, '/', mnames, name, r.status_code
        sleep(delay)

if __name__ == '__main__':
    main()

