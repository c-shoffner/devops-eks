import requests, json, os

terraform_api = os.environ['terraform_api']
url = "https://app.terraform.io/api/v2/workspaces/ws-qam9e7EbmmEhKF6n/current-state-version?include=outputs"
headers = {
  'Authorization': 'Bearer {terraform_api}'
}

response = requests.request("GET", url, headers=headers, data=payload)
response_json = response.json()
values = response_json['included']


for x in values:
    name = x['attributes']['name']
    if 'cluster_name' in name:
        cluster_name = x['attributes']['value']


for x in values:
    name = x['attributes']['name']
    if 'region' in name:
        cluster_region = x['attributes']['value']

os.environ[cluster_name]
os.environ[cluster_region]