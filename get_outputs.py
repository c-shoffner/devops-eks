import requests, json, os, base64

tf_api_token = os.getenv('TF_API_TOKEN')
tf_encoded = str(base64.b64encode(bytes(':{tf_api_token}', 'utf-8')), 'utf-8')
url = "https://app.terraform.io/api/v2/workspaces/ws-qam9e7EbmmEhKF6n/current-state-version?include=outputs"
headers = {
  'Authorization': 'Bearer {tf_encoded}'
}

response = requests.request("GET", url, headers=headers)
print(response)
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