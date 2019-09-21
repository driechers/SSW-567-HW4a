#!/usr/bin/python3

import requests
import json

def get_num_commits(full_name):
    response = requests.get('https://api.github.com/repos/%s/commits' % full_name)
    commits = json.loads(response.text)
    return len(commits)

def get_stats(user):
    response = requests.get('https://api.github.com/users/%s/repos' % user)
    r = ''
    repos = json.loads(response.text)
    for repo in repos:
        r += 'Repo %s ' % repo['name']
        r += 'Number of commits: %d\n' % get_num_commits(repo['full_name'])

    return r

if __name__ == '__main__':
    print(get_stats('driechers'), end='')
