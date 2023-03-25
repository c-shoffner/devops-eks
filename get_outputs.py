import requests, json, os, base64

tf_api_token = os.getenv('TF_API_TOKEN')
url = "https://app.terraform.io/api/v2/workspaces/ws-qam9e7EbmmEhKF6n/current-state-version?include=outputs"
headers = {
  'Authorization': f'Bearer {tf_api_token}'
}
print(headers)
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

env_file = os.getenv("GITHUB_ENV")
with open(env_file, "a") as myfile:
  myfile.write('CLUSTER_NAME={cluster_name}')