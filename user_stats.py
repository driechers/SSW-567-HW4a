#!/usr/bin/python3

import requests
import json
import sys

def get_num_commits(full_name):
    response = requests.get('https://api.github.com/repos/%s/commits' % full_name)

    if response.status_code == 200:
        commits = json.loads(response.text)
        return len(commits)
    else:
        return 0

def get_stats(user):
    response = requests.get('https://api.github.com/users/%s/repos' % user)

    if response.status_code == 200:
        r = ''
        repos = json.loads(response.text)
        for repo in repos:
            r += 'Repo %s ' % repo['name']
            r += 'Number of commits: %d\n' % get_num_commits(repo['full_name'])
        return r
    else:
        return '\n'

if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] == '-h':
        print('Usage:\n\t%s username' % sys.argv[0])
        sys.exit(1)

    print(get_stats(sys.argv[1]), end='')
