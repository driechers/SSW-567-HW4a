#!/usr/bin/python3

import requests

if __name__ == '__main__':
    response = requests.get('https://api.github.com/users/driechers/repos')
    print(response.text)
