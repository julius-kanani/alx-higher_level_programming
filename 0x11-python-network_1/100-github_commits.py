#!/usr/bin/python3
""" 100-github_commits module. Takes two arguments.
    Lists 10 commists (from the most recent to oldest of the a repository.
    The first argument is the repository name.
    The second argument is the owner name of the repository. """
import requests
import sys


if __name__ == "__main__":
    repo_name, owner_name = sys.argv[1], sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
            owner_name, repo_name)
    response = requests.get(url)
    commits = response.json()
    try:
        for i in range(10):
            print("{}: {}".format(
              commits[i].get('sha'),
              commits[i].get('commit').get('author').get('name')))
    except Exception as error:
        pass
