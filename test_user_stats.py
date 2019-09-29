from user_stats import *

import pytest
import requests

def test_num_commits_valid(requests_mock):
    requests_mock.get("https://api.github.com/repos/driechers/2x2x2/commits",
            text=open('test_data/2x2x2_commits','r').read())

    assert get_num_commits('driechers/2x2x2') == 2

def test_num_commits_bad_repo(requests_mock):
    requests_mock.get("https://api.github.com/repos/driechers/NotARepo/commits",
            status_code=404)

    assert get_num_commits('driechers/NotARepo') == 0

def test_num_commits_bad_user(requests_mock):
    requests_mock.get("https://api.github.com/repos/notareallyrealuser/NotARepo/commits",
            status_code=404)

    assert get_num_commits('notareallyrealuser/NotARepo') == 0

def test_stats_valid(requests_mock):
    requests_mock.get("https://api.github.com/users/driechers/repos",
            text=open('test_data/repos','r').read())
    requests_mock.get("https://api.github.com/repos/driechers/2x2x2/commits",
            text=open('test_data/2x2x2_commits','r').read())
    requests_mock.get("https://api.github.com/repos/driechers/asciiquarium/commits",
            text=open('test_data/asciiquarium_commits','r').read())
    requests_mock.get("https://api.github.com/repos/driechers/bijou-snake/commits",
            text=open('test_data/bijou-snake_commits','r').read())
    requests_mock.get("https://api.github.com/repos/driechers/boofuzz/commits",
            text=open('test_data/boofuzz_commits','r').read())
    requests_mock.get("https://api.github.com/repos/driechers/ctags/commits",
            text=open('test_data/ctags_commits','r').read())
    requests_mock.get("https://api.github.com/repos/driechers/grub-invaders/commits",
            text=open('test_data/grub-invaders_commits','r').read())
    requests_mock.get("https://api.github.com/repos/driechers/invaders-before-grub/commits",
            text=open('test_data/invaders-before-grub_commits','r').read())
    requests_mock.get("https://api.github.com/repos/driechers/radascii/commits",
            text=open('test_data/radascii_commits','r').read())
    requests_mock.get("https://api.github.com/repos/driechers/SSW-567/commits",
            text=open('test_data/SSW-567_commits','r').read())
    requests_mock.get("https://api.github.com/repos/driechers/SSW-567-HW01/commits",
            text=open('test_data/SSW-567-HW01_commits','r').read())
    requests_mock.get("https://api.github.com/repos/driechers/SSW-567-HW02a/commits",
            text=open('test_data/SSW-567-HW02a_commits','r').read())
    requests_mock.get("https://api.github.com/repos/driechers/SSW-567-HW4a/commits",
            text=open('test_data/SSW-567-HW4a_commits','r').read())
    requests_mock.get("https://api.github.com/repos/driechers/SSW-567-HW5/commits",
            text=open('test_data/SSW-567-HW5_commits','r').read())

    stats = get_stats('driechers')
    assert stats == \
"""Repo 2x2x2 Number of commits: 2
Repo asciiquarium Number of commits: 12
Repo bijou-snake Number of commits: 17
Repo boofuzz Number of commits: 30
Repo ctags Number of commits: 30
Repo grub-invaders Number of commits: 22
Repo invaders-before-grub Number of commits: 30
Repo radascii Number of commits: 10
Repo SSW-567 Number of commits: 1
Repo SSW-567-HW01 Number of commits: 4
Repo SSW-567-HW02a Number of commits: 7
Repo SSW-567-HW4a Number of commits: 4
Repo SSW-567-HW5 Number of commits: 3
"""

def test_stats_bad_user(requests_mock):
    requests_mock.get("https://api.github.com/users/notareallyrealuser/repos", status_code=404)

    assert get_stats('notareallyrealuser') == '\n'
