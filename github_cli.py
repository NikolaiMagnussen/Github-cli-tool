#!/usr/bin/env python3

import os
import sys
import subprocess
from github import Github, GithubException

key = "change this to your own access key"
owners = [
        # This should contain a list of possible owners you do not want to be affected by the read-only change
]

def print_help():
    print("Usage {} <action> <search string>".format(sys.argv[0]))
    print("Available actions:")
    print("    ls")
    print("    clone")
    print("    set_readonly")

def list_matching(project):
    g = Github(key)
    for repo in g.get_user().get_repos():
        if project in repo.name:
            print(repo.name)

def set_matching_readonly(project):
    g = Github(key)
    for repo in g.get_user().get_repos():
        if project in repo.name:
            print("Changing permissions for {}".format(repo.name))
            for collab in repo.get_collaborators():
                if not collab.login in owners:
                    # Student found. change permissions from push to pull
                    repo.remove_from_collaborators(collab)
                    try:
                        repo.add_to_collaborators(collab, "pull")
                        print("    {} can only read".format(collab.login))
                    except GithubException:
                        repo.add_to_collaborators(collab)
                        print("    {} can still write because readonly is only possible for organizations".format(collab.login))
                else:
                    print("    Owner: {}".format(collab.login))

def clone_matching(project):
    project_dir = "{}/{}".format(os.getcwd(), project)
    g = Github(key)
    for repo in g.get_user().get_repos():
        if project in repo.name:
            if not os.path.isdir(project_dir):
                os.mkdir(project_dir)
            split_idx = repo.clone_url.find("github.com")
            repo_url = "{}{}@{}".format(repo.clone_url[:split_idx], key, repo.clone_url[split_idx:])
            subprocess.run(["git", "clone", repo_url], cwd = project_dir)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print_help()
        sys.exit(1)

    if sys.argv[1] == "ls":
        list_matching(sys.argv[2])
    elif sys.argv[1] == "clone":
        clone_matching(sys.argv[2])
    elif sys.argv[1] == "set_readonly":
        print("Are you sure you want to set all non-owners of the matching repos to read-only?")
        print("Type 'YES' to confirm")
        ans = input()
        if ans == "YES":
            set_matching_readonly(sys.argv[2])
    else:
        print_help()
