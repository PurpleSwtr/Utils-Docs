import os

import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
REPO_OWNER = os.getenv("REPO_OWNER")
REPO_NAME = os.getenv("REPO_NAME")
WORKFLOW_NAME = os.getenv("WORKFLOW_NAME")

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/actions/workflows/{WORKFLOW_NAME}/runs"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    runs = response.json().get("workflow_runs", [])
    print(runs)
    if runs:
        latest_run = runs[0]
        print(f"Статус: {latest_run['status']} - {latest_run['conclusion']}")
else:
    print(f"{response.status_code} - {response.json()}")
