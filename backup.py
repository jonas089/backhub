import requests
import json
import subprocess


def format_args(list):
	return "\n".join(list) + "\n"

username = str(input("Enter username (str): "))
per_page = int(input("Enter per_page (int): "))
output_path = str(input("Output path (str): "))
repos = []

projects = json.loads(requests.get("https://api.github.com/users/{username}/repos?per_page={per_page}".format(username=username, per_page=str(per_page))).text)

for project in projects:
	repos.append(project["name"])

process = subprocess.Popen(["./clone_profile.sh", username, output_path], stdin=subprocess.PIPE)
process.stdin.write(format_args(repos).encode('utf-8'))
process.stdin.close()
process.wait()
