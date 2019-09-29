from user_stats import *

import pytest
import requests

def test_num_commits_valid(requests_mock):
    requests_mock.get("https://api.github.com/repos/driechers/2x2x2/commits",
            text=open('test_data/2x2x2_commits','r').read())

    assert get_num_commits('driechers/2x2x2') == 2

def test_num_commits_bad_repo():
    assert get_num_commits('driechers/NotARepo') == 0

def test_num_commits_bad_user():
    assert get_num_commits('notareallyrealuser/NotARepo') == 0

#def test_stats_valid(requests_mock):
#    requests_mock.get("https://api.github.com/users/driechers/repos", text='[]')
#    stats = get_stats('driechers')
#    assert stats[:-2] == \
#"""Repo 2x2x2 Number of commits: 2
#Repo asciiquarium Number of commits: 12
#Repo bijou-snake Number of commits: 17
#Repo boofuzz Number of commits: 30
#Repo ctags Number of commits: 30
#Repo grub-invaders Number of commits: 22
#Repo invaders-before-grub Number of commits: 30
#Repo radascii Number of commits: 10
#Repo SSW-567 Number of commits: 1
#Repo SSW-567-HW01 Number of commits: 4
#Repo SSW-567-HW02a Number of commits: 7
#Repo SSW-567-HW4a Number of commits: """

#def test_stats_bad_user():
#    assert get_stats('notareallyrealuser') == '\n'
