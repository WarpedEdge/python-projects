import requests

response = requests.get("https://www.gitlab.com/api/v4/users/nanuchi/projects")
my_projects = response.json()

for project in my_projects:
    print(f"Project name: {project['name']}\nProject Url: {project['web_url']}\n")

